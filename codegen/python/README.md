# Python Code Generation

This directory contains configuration files for generating Python code from OpenAPI specifications.

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
# Generate Python code
task generate-python

# Or generate all languages
task generate
```

## Generated Files

```
gen/python/
├── models.py                    # Pydantic models
└── server/                      # FastAPI server code
    ├── openapi_server/
    │   ├── apis/               # API route handlers
    │   ├── models/             # Request/response models
    │   └── main.py             # FastAPI app
    ├── impl/                   # Implementation stubs
    └── requirements.txt        # Python dependencies
```

## Implementation Example

### Using Generated Models

```python
from gen.python.models import Card, CardsCreateRequestPayload

# Create a new card
card_data = CardsCreateRequestPayload(
    number="4532-1234-5678-9012",
    title="My Credit Card",
    status="active"
)

# Use the generated model
card = Card(
    id="card_123",
    number=card_data.number,
    title=card_data.title,
    status=card_data.status,
    created_at="2024-01-15T10:30:00Z"
)
```

### Using Generated FastAPI Server

```python
from fastapi import FastAPI
from gen.python.server.openapi_server.apis.cards_api import router as cards_router

app = FastAPI(title="Contracts API")
app.include_router(cards_router, prefix="/v1")

# Implement handlers in impl/ directory
```

## Dependencies

Add to your `requirements.txt`:

```txt
fastapi>=0.104.0
pydantic>=2.5.0
uvicorn>=0.24.0
```

## Development

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Generate code**: `task generate-python`
3. **Implement business logic** in the `impl/` directory
4. **Run server**: `uvicorn main:app --reload --port 8000`

## Features

- **Type Safety**: Full type hints with Pydantic validation
- **Auto Documentation**: FastAPI generates OpenAPI docs automatically
- **Validation**: Request/response validation out of the box
- **Modern Python**: Uses latest Python features and best practices 