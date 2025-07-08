# Go Code Generation

This directory contains configuration files for generating Go code from OpenAPI specifications using [oapi-codegen](https://github.com/deepmap/oapi-codegen).

## Configuration Files

### `models.yaml`
Generates Go structs and types from OpenAPI schema definitions.

**Configuration:**
- **Package**: `contracts`
- **Output**: `gen/go/models.gen.go`
- **Generates**: Data models, enums, request/response types
- **Features**: JSON tags, validation, type safety

### `server.yaml`
Generates Chi router server handlers and interfaces.

**Configuration:**
- **Package**: `contracts`
- **Output**: `gen/go/server.gen.go`
- **Generates**: Server interfaces, Chi router handlers, middleware
- **Features**: Chi router, strict server mode, type-safe handlers

## Usage

```bash
# Generate Go code
task generate-go

# Or generate all languages
task generate
```

## Generated Files

- `gen/go/models.gen.go` - Type definitions and data models
- `gen/go/server.gen.go` - Chi server handlers and interfaces

## Implementation Example

```go
package main

import (
    "net/http"
    "github.com/go-chi/chi/v5"
    "your-module/gen/go"
)

type Server struct{}

func (s *Server) GetCards(w http.ResponseWriter, r *http.Request) {
    // Implementation
}

func (s *Server) CreateCard(w http.ResponseWriter, r *http.Request) {
    // Implementation
}

func main() {
    server := &Server{}
    r := chi.NewRouter()
    handler := contracts.HandlerFromMux(server, r)
    http.ListenAndServe(":8080", handler)
}
```

## oapi-codegen Features Used

- **chi-server**: Chi router integration
- **strict-server**: Type-safe request/response handling
- **models**: Go struct generation
- **skip-prune**: Keep all generated types 