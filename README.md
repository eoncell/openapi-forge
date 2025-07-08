# Contracts Blueprint

A clean OpenAPI contract generation blueprint demonstrating modular schema architecture with multi-language code generation for Go, Python, and TypeScript.

## 🎯 Purpose

This blueprint shows how to structure OpenAPI specifications for:
- **Clean contract generation** across multiple languages
- **Modular schema architecture** using `$ref` patterns
- **Maintainable API specifications** with separation of concerns

## 🏗️ Architecture Philosophy

### Modular Schema Design
- Separate schema files for reusability
- `$ref` instead of inline definitions
- Domain-based organization (auth, users, common)

### Multi-Language Generation
- Same OpenAPI spec → multiple language implementations
- Language-specific configurations in `codegen/`
- Generated code in `gen/` (never edit directly)

## 📁 Project Structure

```
contracts-blueprint/
├── 📁 src/                         # OpenAPI source definitions
│   ├── 📄 openapi.yaml            # Main API specification
│   ├── 📁 resources/              # API endpoint definitions  
│   │   ├── 📁 auth/               # Authentication endpoints
│   │   ├── 📁 health/             # Health check endpoints
│   │   └── 📁 users/              # User management endpoints
│   └── 📁 schemas/                # Reusable schema components
│       ├── 📁 common/             # Shared schemas (Email, UUID, etc.)
│       ├── 📁 auth/               # Authentication schemas
│       └── 📁 users/              # User-related schemas
├── 📁 codegen/                    # Language-specific configurations
│   ├── 📁 go/                     # Go generation configs
│   ├── 📁 python/                 # Python generation configs  
│   └── 📁 typescript/             # TypeScript generation configs
├── 📁 gen/                        # Generated code output
├── 📁 openapi/                    # Bundled OpenAPI specifications
└── 📄 [Root Files]                # Configuration and build files
```

## 📂 Root Files Description

| File | Purpose | Description |
|------|---------|-------------|
| `📄 .gitignore` | Git Configuration | Excludes generated files, dependencies, and system files |
| `📄 .spectral.yaml` | API Linting | Spectral configuration for OpenAPI quality checks |
| `📄 bun.lockb` | Dependency Lock | Bun lockfile for reproducible builds |  
| `📄 go.mod` | Go Dependencies | Go module with oapi-codegen dependencies |
| `📄 go.sum` | Go Checksums | Cryptographic checksums for Go dependencies |
| `📄 openapitools.json` | Generator Config | Version lock (7.14.0) for consistency |
| `📄 package.json` | Node.js Config | Dependencies and scripts for TypeScript generation |
| `📄 README.md` | Documentation | This file - project documentation |
| `📄 Taskfile.yml` | Build Automation | Task runner for building and generating |

## 🔧 Available Tasks

```bash
# Core Development
task install       # Install all dependencies
task build         # Bundle OpenAPI spec to openapi/openapi.yaml
task generate      # Generate code for all languages
task lint          # Lint OpenAPI specification
task clean         # Remove generated files

# Language-Specific Generation  
task generate-go        # Generate Go models and server
task generate-python    # Generate Python models and server
task generate-typescript # Generate TypeScript client and types

# Full Pipeline
task all           # Complete build: install → build → generate → lint
```

## 🚀 Usage Examples

### 1. Generate Go Server & Import as Module

```bash
# Generate Go server code
task generate-go

# Create a new Go service that uses the generated contracts
mkdir my-auth-service
cd my-auth-service
go mod init github.com/myuser/my-auth-service

# Import the generated contracts
go get github.com/eoncell/openapi-forge@v1.0.0
```

**Using in your Go service:**
```go
package main

import (
    "github.com/eoncell/openapi-forge/gen/go"
    "github.com/go-chi/chi/v5"
)

func main() {
    r := chi.NewRouter()
    
    // Use generated server interface
    server := &AuthServer{}
    contracts.HandlerFromMux(server, r)
    
    http.ListenAndServe(":8080", r)
}

// Implement the generated interface
type AuthServer struct{}

func (s *AuthServer) PostAuthLogin(w http.ResponseWriter, r *http.Request) {
    // Your implementation here
}
```

### 2. Version Your Generated Contracts

```bash
# After generating code and testing
git add .
git commit -m "feat: add user management endpoints"

# Tag for versioning
git tag v1.0.0
git push origin v1.0.0

# Now other projects can import specific versions
go get github.com/eoncell/openapi-forge@v1.0.0
```

### 3. Python FastAPI Service

```bash
# Generate Python server
task generate-python

# Create new Python service
mkdir my-python-service
cd my-python-service
pip install fastapi uvicorn

# Install your contracts package
pip install git+https://github.com/eoncell/openapi-forge.git@v1.0.0
```

**Using in your Python service:**
```python
from fastapi import FastAPI
from openapi_forge.models import User, AuthRequestPayload
from openapi_forge.server import AuthApi

app = FastAPI()

@app.post("/auth/login")
async def login(payload: AuthRequestPayload):
    # Your implementation using generated models
    return {"access_token": "...", "token_type": "bearer"}
```

### 4. TypeScript Client Integration

```bash
# Generate TypeScript client
task generate-typescript

# In your frontend project
npm install @eoncell/openapi-forge@1.0.0
```

**Using in your TypeScript app:**
```typescript
import { AuthApi, User } from '@eoncell/openapi-forge';

const authApi = new AuthApi();

// Type-safe API calls
const login = async (email: string, password: string) => {
  const response = await authApi.postAuthLogin({
    email,
    password
  });
  return response.data;
};
```

### 5. Full Development Workflow

```bash
# 1. Modify API specification
vim src/resources/users/users.yaml

# 2. Generate and test
task generate
task lint

# 3. Test in your service
cd ../my-auth-service
go mod tidy
go run main.go

# 4. Version and release
git add .
git commit -m "feat: add user profile endpoints"
git tag v1.1.0
git push origin v1.1.0

# 5. Update consumers
cd ../my-python-service
pip install --upgrade git+https://github.com/eoncell/openapi-forge.git@v1.1.0
```

### 6. Multiple Services Pattern

```
your-microservices/
├── contracts/                 # This openapi-forge project
├── auth-service/             # Go service using contracts@v1.0.0
├── user-service/             # Python service using contracts@v1.0.0  
├── frontend/                 # React app using contracts@v1.0.0
└── mobile-app/               # React Native using contracts@v1.0.0
```

**Benefits:**
- ✅ Single source of truth for API contracts
- ✅ Type safety across all services
- ✅ Versioned contracts prevent breaking changes
- ✅ Auto-generated clients reduce boilerplate

## 🏛️ Schema Architecture

### 📦 Common Schemas (`src/schemas/common/`)
- `Email.yaml` - Email format validation
- `Password.yaml` - Password requirements
- `UUID.yaml` - Standard UUID format

### 🔐 Auth Schemas (`src/schemas/auth/`)
- `AuthRequestPayload.yaml` - Login credentials
- `SignUpRequestPayload.yaml` - Registration data
- `TokenResponse.yaml` - Auth response

### 👥 User Schemas (`src/schemas/users/`)
- `User.yaml` - User entity
- `UserCreateRequest.yaml` - User creation
- `UserUpdateRequest.yaml` - User updates

## 🛠️ Generation Tools

### 🐹 Go - `oapi-codegen` v2
- Generates Chi router and models
- Struct types with JSON tags
- Built-in validation

### 🐍 Python - `datamodel-code-generator` + `openapi-generator`
- Pydantic v2 models with validation
- FastAPI server generation
- Type hints and runtime validation

### 🟦 TypeScript - `@hey-api/openapi-ts`
- Modern Fetch API client
- Complete TypeScript interfaces
- Tree-shakeable imports

## 📋 Key Patterns

### 1. Schema Reusability
```yaml
# Instead of inline schemas
properties:
  email:
    type: string
    format: email

# Use $ref for reusability
properties:
  email:
    $ref: '../common/Email.yaml'
```

### 2. Domain Organization
```
schemas/
├── common/     # Shared across domains
├── auth/       # Authentication specific
└── users/      # User management specific
```

### 3. Clean Separation
```
resources/
├── auth/       # Auth endpoints
├── health/     # Health checks
└── users/      # User CRUD
```

## 🚀 Adding New Domains

```bash
# 1. Create schema files
mkdir -p src/schemas/products
touch src/schemas/products/Product.yaml

# 2. Create endpoint files  
mkdir -p src/resources/products
touch src/resources/products/products.yaml

# 3. Update main spec
# Edit src/openapi.yaml to include new paths

# 4. Generate
task generate
```

## 🎯 Best Practices

### Schema Design
- ✅ Use `$ref` for reusability
- ✅ Keep schemas atomic and focused
- ✅ Organize by domain, not by type
- ✅ Include examples in schemas

### File Organization
- ✅ Separate endpoints by domain
- ✅ Use descriptive file names
- ✅ Keep configurations language-specific
- ✅ Never edit generated code directly

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `task all`
5. Submit a pull request

## 📜 License

MIT License - see LICENSE file for details.

---

⭐ **Star this repo** if you find it helpful! 

💬 **Questions?** Open an issue or start a discussion.

🐛 **Found a bug?** Please report it with details to reproduce.
