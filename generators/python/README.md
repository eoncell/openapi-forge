# Python Code Generator

This directory contains the **Application Layer** toolchain for generating Python adapters from OpenAPI specifications.

## Architecture Role

In OpenAPI Forge's Clean Architecture:
- **Domain Layer** (`api/`): OpenAPI specifications as single source of truth
- **Application Layer** (`generators/python/`): **← You are here** - Python-specific toolchain with isolated dependencies
- **Infrastructure Layer** (`adapters/python/`): Production-ready generated Python code

## Tools Used

### `datamodel-code-generator`
Generates Pydantic v2 models from OpenAPI schema definitions.

**Features:**
- Pydantic v2 BaseModel generation
- Type annotations with validation
- Field descriptions and constraints
- Python 3.11+ compatibility

### `openapi-generator`
Generates FastAPI server code from OpenAPI specifications.

**Features:**
- FastAPI server skeleton
- Router and endpoint definitions
- Request/response models integration
- Implementation stubs

## Configuration Files

### `models.yaml`
Configuration for Pydantic model generation using `datamodel-code-generator`.

**Key settings:**
- **Output**: Pydantic v2 BaseModel
- **Python version**: 3.11+
- **Features**: Field constraints, annotations, snake_case fields
- **Type safety**: Strict types for primitives

### `fastapi.yaml`
Configuration for FastAPI server generation using `openapi-generator`.

**Key settings:**
- **Package**: contracts
- **Port**: 8000
- **Implementation**: Separate impl package for business logic

## Usage

```bash
# Generate Python adapters
task generate-python

# Or generate all language adapters
task generate
```

## Generated Adapters

```
adapters/python/
├── models.py                    # Pydantic models
└── server/                      # FastAPI server code
    ├── src/contracts/
    │   ├── apis/               # API route handlers
    │   ├── models/             # Request/response models
    │   └── main.py             # FastAPI app
    ├── impl/                   # Implementation stubs
    └── requirements.txt        # Python dependencies
```

## Implementation Example

### Using Generated Models

```python
from adapters.python.models import User, UserCreateRequest

# Create a new user
user_data = UserCreateRequest(
    name="John Doe",
    email="john@example.com",
    role="user"
)

# Use the generated model
user = User(
    id="user_123",
    name=user_data.name,
    email=user_data.email,
    role=user_data.role,
    status="active",
    created_at="2024-01-15T10:30:00Z"
)
```

### Using Generated FastAPI Server

```python
from fastapi import FastAPI
from adapters.python.server.src.contracts.apis.users_api import router as users_router
from adapters.python.server.src.contracts.apis.authentication_api import router as auth_router

app = FastAPI(title="OpenAPI Forge API")
app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")

# Implement handlers in impl/ directory
```

## Dependencies

This generator includes its own isolated dependencies:

```txt
# generators/python/requirements.txt
datamodel-code-generator>=0.25.0
openapi-generator-cli>=7.2.0
```

For your application, add to your `requirements.txt`:

```txt
fastapi>=0.104.0
pydantic>=2.5.0
uvicorn>=0.24.0
```

## Development

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Generate adapters**: `task generate-python`
3. **Implement business logic** in the `impl/` directory
4. **Run server**: `uvicorn main:app --reload --port 8000`

## Features

- **Type Safety**: Full type hints with Pydantic validation
- **Auto Documentation**: FastAPI generates OpenAPI docs automatically
- **Validation**: Request/response validation out of the box
- **Modern Python**: Uses latest Python features and best practices
- **Clean Separation**: Business logic separated from HTTP concerns

## Clean Architecture Benefits

1. **Isolated Dependencies**: Python toolchain dependencies don't pollute other language generators
2. **Adapter Pattern**: Generated code provides clean interfaces for your business logic
3. **Domain Independence**: Business logic remains separate from HTTP concerns
4. **Type Safety**: Runtime validation and static type checking
5. **Testability**: Clean interfaces make unit testing straightforward 