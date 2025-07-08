# OpenAPI Forge

A modern OpenAPI code generation tool built with Clean Architecture principles, enabling multi-language code generation for Go, Python, and TypeScript from a single API specification.

## 🎯 Purpose

OpenAPI Forge demonstrates how to build enterprise-grade API tooling with:
- **Clean Architecture** separation of concerns
- **Multi-language code generation** from single source of truth
- **Developer-friendly** project structure and workflows
- **Production-ready** generated adapters

## 🏗️ Clean Architecture Philosophy

### Domain Layer: `api/`
- **Single source of truth** for API specifications
- **Modular schema design** using `$ref` patterns
- **Domain-driven organization** (auth, users, common)

### Application Layer: `generators/`
- **Language-specific toolchains** with isolated dependencies
- **Generation configurations** tailored per technology
- **Build automation** and dependency management

### Infrastructure Layer: `adapters/`
- **Ready-to-use code** generated from specifications
- **Language-native implementations** (Go servers, Python FastAPI, TypeScript clients)
- **Production-ready** with proper typing and validation

## 📁 Project Structure

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

## 🚀 Quick Start

```bash
# 1. Install dependencies
task install

# 2. Generate all adapters
task generate

# 3. View generated code
ls adapters/go/
ls adapters/python/
ls adapters/typescript/
```

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

## 🛠️ Language Generators

Each generator is a self-contained toolchain in the Application Layer:

### 🐹 Go Generator
- **Location**: `generators/go/`
- **Tools**: oapi-codegen v2 with Chi router
- **Output**: Server interfaces, models, middleware
- **📖 Full Documentation**: [generators/go/README.md](generators/go/README.md)

### 🐍 Python Generator
- **Location**: `generators/python/`
- **Tools**: datamodel-code-generator + openapi-generator
- **Output**: FastAPI server, Pydantic models
- **📖 Full Documentation**: [generators/python/README.md](generators/python/README.md)

### 🟦 TypeScript Generator
- **Location**: `generators/typescript/`
- **Tools**: @hey-api/openapi-ts
- **Output**: Fetch client, complete type definitions
- **📖 Full Documentation**: [generators/typescript/README.md](generators/typescript/README.md)

## 🏛️ Schema Architecture

### 📦 Common Schemas (`api/schemas/common/`)
Reusable components across all domains:
- `Email.yaml`, `Password.yaml`, `Id.yaml`
- `PaginationMeta.yaml`, `Order.yaml`

### 🔐 Auth Schemas (`api/schemas/auth/`)
Authentication and authorization:
- `AuthRequestPayload.yaml`, `TokenResponse.yaml`
- `RegisterRequestPayload.yaml`

### 👥 User Schemas (`api/schemas/users/`)
User management domain:
- `User.yaml`, `UserCreateRequest.yaml`
- `UserUpdateRequest.yaml`, `UserRole.yaml`

## 📋 Development Workflow

### 1. API-First Development
```bash
# Design your API in api/openapi.yaml
vim api/resources/users/users.yaml

# Generate adapters
task generate

# Use in your services
cp -r adapters/go/ ../my-go-service/contracts/
cp -r adapters/python/ ../my-python-service/contracts/
cp -r adapters/typescript/ ../my-frontend/api-client/
```

### 2. Integration Examples

#### Go Service
```go
import "your-module/adapters/go"

type Server struct{}
func (s *Server) GetUsers(w http.ResponseWriter, r *http.Request) {
    // Implementation using generated types
}
```

#### Python Service
```python
from adapters.python.models import User, UserCreateRequest
from adapters.python.server.src.contracts.apis.users_api_base import BaseUsersApi

class UsersService(BaseUsersApi):
    def get_users(self, limit: int = 10, offset: int = 0):
        # Implementation
        pass
```

#### TypeScript Client
```typescript
import { UsersService } from './adapters/typescript/client';
import type { User } from './adapters/typescript/types';

const users: User[] = await UsersService.getUserList();
```

## ✨ Clean Architecture Benefits

### 🎯 Separation of Concerns
- **API specifications** remain pure and language-agnostic
- **Generators** are isolated with their own dependencies
- **Adapters** are production-ready without manual modifications

### 🔄 Dependency Isolation
Each generator has its own dependency management:
- **Go**: `generators/go/go.mod`
- **Python**: `generators/python/requirements.txt`
- **TypeScript**: `generators/typescript/package.json`

### 🚀 Enterprise Benefits
- **Single Source of Truth**: API contract drives all implementations
- **Type Safety**: Generated code provides compile-time validation
- **Consistency**: Same business logic across all language implementations
- **Maintainability**: Changes in API automatically propagate to all clients/servers

## 🚀 Adding New Domains

```bash
# 1. Create schema files
mkdir -p api/schemas/products
touch api/schemas/products/Product.yaml

# 2. Create endpoint files  
mkdir -p api/resources/products
touch api/resources/products/products.yaml

# 3. Update main spec
# Edit api/openapi.yaml to include new paths

# 4. Generate adapters
task generate
```

## 📋 File Organization

### 🎯 `api/` - API Specifications (Domain Layer)
- `openapi.yaml` - Main API specification
- `resources/` - Endpoint definitions by domain
- `schemas/` - Reusable data models
- `parameters/` - Shared parameters

### 🔧 `generators/` - Code Generators (Application Layer)
- Language-specific toolchains with isolated dependencies
- See individual README files for detailed documentation

### ⚡ `adapters/` - Generated Adapters (Infrastructure Layer)
- Production-ready code generated from specifications
- Copy these into your services/applications

### 🛠️ Root Configuration
| File | Purpose |
|------|---------|
| `📄 Taskfile.yml` | Build automation and task orchestration |
| `📄 package.json` | Core tooling (Redocly, Spectral) |
| `📄 .spectral.yaml` | API linting rules |

## 🎯 Best Practices

### Schema Design
- ✅ Use `$ref` for reusability
- ✅ Keep schemas atomic and focused
- ✅ Organize by domain, not by type
- ✅ Include examples in schemas

### Development Workflow
- ✅ Design API first in `api/openapi.yaml`
- ✅ Generate adapters with `task generate`
- ✅ Copy adapters to your services
- ✅ Implement business logic using generated types

### Versioning
- ✅ Version your API specifications
- ✅ Tag releases after breaking changes
- ✅ Update all consuming services

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
