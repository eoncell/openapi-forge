# Go Code Generator

This directory contains the **Application Layer** toolchain for generating Go adapters from OpenAPI specifications using [oapi-codegen](https://github.com/deepmap/oapi-codegen).

## Architecture Role

In OpenAPI Forge's Clean Architecture:
- **Domain Layer** (`api/`): OpenAPI specifications as single source of truth
- **Application Layer** (`generators/go/`): **← You are here** - Go-specific toolchain with isolated dependencies
- **Infrastructure Layer** (`adapters/go/`): Production-ready generated Go code

## Configuration Files

### `models.yaml`
Generates Go structs and types from OpenAPI schema definitions.

**Configuration:**
- **Package**: `contracts`
- **Output**: `adapters/go/models.gen.go`
- **Generates**: Data models, enums, request/response types
- **Features**: JSON tags, validation, type safety

### `server.yaml`
Generates Chi router server handlers and interfaces.

**Configuration:**
- **Package**: `contracts`
- **Output**: `adapters/go/server.gen.go`
- **Generates**: Server interfaces, Chi router handlers, middleware
- **Features**: Chi router, strict server mode, type-safe handlers

## Usage

```bash
# Generate Go adapters
task generate-go

# Or generate all language adapters
task generate
```

## Generated Adapters

- `adapters/go/models.gen.go` - Type definitions and data models
- `adapters/go/server.gen.go` - Chi server handlers and interfaces

## Implementation Example

```go
package main

import (
    "net/http"
    "github.com/go-chi/chi/v5"
    "your-module/adapters/go"
)

type Server struct{}

func (s *Server) GetHealth(w http.ResponseWriter, r *http.Request) {
    // Implementation
}

func (s *Server) AuthenticateUser(w http.ResponseWriter, r *http.Request) {
    // Implementation
}

func (s *Server) GetUsers(w http.ResponseWriter, r *http.Request) {
    // Implementation
}

func main() {
    server := &Server{}
    r := chi.NewRouter()
    handler := contracts.HandlerFromMux(server, r)
    http.ListenAndServe(":8080", handler)
}
```

## Dependencies

This generator includes its own `go.mod` with isolated dependencies:

```go
module github.com/your-org/openapi-forge/generators/go

go 1.23.3

require (
    github.com/deepmap/oapi-codegen/v2 v2.1.0
    github.com/go-chi/chi/v5 v5.0.10
)
```

## oapi-codegen Features Used

- **chi-server**: Chi router integration
- **strict-server**: Type-safe request/response handling
- **models**: Go struct generation
- **skip-prune**: Keep all generated types

## Clean Architecture Benefits

1. **Isolated Dependencies**: Go toolchain dependencies don't pollute other language generators
2. **Adapter Pattern**: Generated code provides clean interfaces for your business logic
3. **Domain Independence**: Business logic remains separate from HTTP concerns
4. **Type Safety**: Compile-time guarantees for API contracts 