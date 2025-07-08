# OpenAPI Forge

A **template** for creating API contract repositories with Clean Architecture principles, enabling multi-language code generation for Go, Python, and TypeScript from a single API specification.

> 🎯 **This is a blueprint/template** - copy it to create your own API contracts repository!

## 🎯 Purpose

OpenAPI Forge demonstrates how to build enterprise-grade API tooling with:
- **Clean Architecture** separation of concerns
- **Multi-language code generation** from single source of truth
- **Developer-friendly** project structure and workflows
- **Production-ready** generated adapters

## 🚀 Quick Start

### 1. Create Your API Contracts Repository

```bash
# Use this repository as a template for your own API contracts
git clone https://github.com/eoncell/openapi-forge.git my-api-contracts
cd my-api-contracts

# Make it your own repository
rm -rf .git
git init
git remote add origin https://github.com/mycompany/my-api-contracts.git

# Install dependencies
task install
```

### 2. Design Your API

```bash
# Customize the API specifications for your domain
vim api/resources/users/users.yaml
vim api/schemas/users/User.yaml

# Generate adapters from your specifications
task generate

# Verify everything works
ls adapters/go/
ls adapters/python/
ls adapters/typescript/
```

### 3. Publish Your Contracts

```bash
# Commit and publish your API contracts
git add .
git commit -m "feat: initial API contracts"
git push origin main

# Tag a version for consumption
git tag v1.0.0
git push origin v1.0.0
```

## 📦 Using Your Contracts in Projects

Now that you've published your contracts, here's how to import them in your services:

### **Go Service**
```go
// go.mod
module github.com/mycompany/user-service

require (
    github.com/mycompany/my-api-contracts/adapters/go v1.0.0
)

// main.go
import (
    "github.com/mycompany/my-api-contracts/adapters/go"
    "github.com/go-chi/chi/v5"
)

func main() {
    server := &MyServer{}
    r := chi.NewRouter()
    contracts.HandlerFromMux(server, r)
    http.ListenAndServe(":8080", r)
}
```

### **Python Service**
```python
# requirements.txt
git+https://github.com/mycompany/my-api-contracts.git@v1.0.0#subdirectory=adapters/python

# main.py
from adapters.python.models import User, UserCreateRequest
from adapters.python.server.src.contracts.apis.users_api_base import BaseUsersApi

class UsersService(BaseUsersApi):
    def get_users(self, limit: int = 10, offset: int = 0):
        # Your implementation
        pass
```

### **TypeScript Client**
```typescript
// package.json
{
  "dependencies": {
    "my-api-contracts": "github:mycompany/my-api-contracts#v1.0.0"
  }
}

// app.ts
import { UsersService } from 'my-api-contracts/adapters/typescript/client';
import type { User } from 'my-api-contracts/adapters/typescript/types';

const users: User[] = await UsersService.getUserList();
```

## 🏗️ Project Structure

```
openapi-forge/
├── api/                    # API specifications (Domain Layer)
│   ├── openapi.yaml       # Main OpenAPI spec
│   ├── parameters/        # Reusable parameters
│   ├── resources/         # API endpoint definitions
│   └── schemas/           # Data models and schemas
├── generators/            # Code generators (Application Layer)
│   ├── go/               # Go toolchain → See generators/go/README.md
│   ├── python/           # Python toolchain → See generators/python/README.md
│   └── typescript/       # TypeScript toolchain → See generators/typescript/README.md
├── adapters/             # Generated adapters (Infrastructure Layer)
│   ├── go/              # Go server + models
│   ├── python/          # FastAPI server + models
│   └── typescript/      # TypeScript client + types
├── openapi/             # Bundled OpenAPI spec
├── package.json         # Core tooling (Redocly, Spectral)
└── Taskfile.yml         # Build automation
```

### `api/` - API Specifications (Domain Layer)
- `openapi.yaml` - Main API specification
- `resources/` - Endpoint definitions by domain
- `schemas/` - Reusable data models
- `parameters/` - Shared parameters

### `generators/` - Code Generators (Application Layer)
Language-specific toolchains with isolated dependencies:

#### 🐹 Go Generator (`generators/go/`)
- **Tools**: oapi-codegen v2 with Chi router
- **Output**: Server interfaces, models, middleware
- **📖 Full Documentation**: [generators/go/README.md](generators/go/README.md)

#### 🐍 Python Generator (`generators/python/`)
- **Tools**: datamodel-code-generator + openapi-generator
- **Output**: FastAPI server, Pydantic models
- **📖 Full Documentation**: [generators/python/README.md](generators/python/README.md)

#### 🟦 TypeScript Generator (`generators/typescript/`)
- **Tools**: @hey-api/openapi-ts
- **Output**: Fetch client, complete type definitions
- **📖 Full Documentation**: [generators/typescript/README.md](generators/typescript/README.md)

### `adapters/` - Generated Adapters (Infrastructure Layer)
- Production-ready code generated from specifications
- Import these as packages in your services/applications

### 🛠️ Root Configuration
| File | Purpose |
|------|---------|
| `📄 Taskfile.yml` | Build automation and task orchestration |
| `📄 package.json` | Core tooling (Redocly, Spectral) |
| `📄 .spectral.yaml` | API linting rules |

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



## 🎯 Best Practices

### Schema Design
- ✅ Use `$ref` for reusability
- ✅ Keep schemas atomic and focused
- ✅ Organize by domain, not by type
- ✅ Include examples in schemas

### Development Workflow
- ✅ Design API first in `api/openapi.yaml`
- ✅ Generate adapters with `task generate`
- ✅ Import adapters as packages (not copy!)
- ✅ Implement business logic using generated types

### Versioning
- ✅ Version your API specifications
- ✅ Tag releases after breaking changes
- ✅ Update all consuming services

## 🚀 Benefits

- **Single Source of Truth**: API contract drives all implementations
- **Type Safety**: Generated code provides compile-time validation
- **Consistency**: Same business logic across all language implementations
- **Maintainability**: Changes in API automatically propagate to all clients/servers

## 🔍 Need More Details?

- **Go Generator**: [generators/go/README.md](generators/go/README.md)
- **Python Generator**: [generators/python/README.md](generators/python/README.md)
- **TypeScript Generator**: [generators/typescript/README.md](generators/typescript/README.md)

Each generator README contains:
- Detailed tool configuration
- Advanced usage examples
- Implementation patterns
- Dependencies and setup
- Troubleshooting guides

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
