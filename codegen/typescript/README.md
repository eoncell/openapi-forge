# TypeScript Code Generation

This directory contains configuration files for generating TypeScript code from OpenAPI specifications.

## Tools Used

### `@hey-api/openapi-ts`
Modern TypeScript client generator with excellent OpenAPI support.

**Features:**
- TypeScript types and interfaces
- HTTP client with Fetch API
- Tree-shakeable exports
- Full OpenAPI 3.x support
- Modern JavaScript/TypeScript patterns

## Configuration Files

### `client.yaml`
Configuration for full TypeScript client generation.

**Key settings:**
- **Client**: @hey-api/client-fetch (modern Fetch API)
- **Plugins**: Schemas, SDK, TypeScript types
- **Output**: Formatted and linted code

### `types.yaml`
Configuration for TypeScript types-only generation.

**Key settings:**
- **Plugin**: TypeScript types only
- **Output**: Clean type definitions without client code

## Usage

```bash
# Generate TypeScript code
task generate-typescript

# Or generate all languages
task generate
```

## Generated Files

```
gen/typescript/
├── client/                      # Full client with SDK
│   ├── types.gen.ts            # TypeScript types
│   ├── services.gen.ts         # API service methods
│   ├── schemas.gen.ts          # Schema definitions
│   └── index.ts                # Main exports
└── types/                      # Types-only generation
    ├── types.gen.ts            # TypeScript interfaces
    └── index.ts                # Type exports
```

## Implementation Examples

### Using Generated Client

```typescript
import { CardsService, type Card, type CardsCreateRequestPayload } from './gen/typescript/client';

// Configure the client
import { OpenAPI } from './gen/typescript/client';
OpenAPI.BASE = 'https://api.example.com';
OpenAPI.TOKEN = 'your-auth-token';

// Use the generated client
async function createCard() {
  const newCard: CardsCreateRequestPayload = {
    number: "4532-1234-5678-9012",
    title: "My Credit Card",
    status: "active"
  };

  try {
    const card: Card = await CardsService.createCard(newCard);
    console.log('Created card:', card);
  } catch (error) {
    console.error('Failed to create card:', error);
  }
}

// List cards
async function listCards() {
  try {
    const cards: Card[] = await CardsService.getCards();
    console.log('Cards:', cards);
  } catch (error) {
    console.error('Failed to fetch cards:', error);
  }
}
```

### Using Types Only

```typescript
import type { Card, CardsCreateRequestPayload } from './gen/typescript/types';

// Use types for your own implementations
interface CardRepository {
  create(data: CardsCreateRequestPayload): Promise<Card>;
  findAll(): Promise<Card[]>;
  findById(id: string): Promise<Card | null>;
}

class CardService implements CardRepository {
  async create(data: CardsCreateRequestPayload): Promise<Card> {
    // Your implementation
    return fetch('/api/v1/cards', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(res => res.json());
  }

  // ... other methods
}
```

### React/Vue/Angular Integration

```typescript
import { CardsService, type Card } from './gen/typescript/client';

// React example
import { useState, useEffect } from 'react';

function CardsComponent() {
  const [cards, setCards] = useState<Card[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    CardsService.getCards()
      .then(setCards)
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {cards.map(card => (
        <div key={card.id}>
          <h3>{card.title}</h3>
          <p>Number: {card.number}</p>
          <p>Status: {card.status}</p>
        </div>
      ))}
    </div>
  );
}
```

## Dependencies

Add to your `package.json`:

```json
{
  "dependencies": {
    "@hey-api/client-fetch": "^0.2.0"
  },
  "devDependencies": {
    "@hey-api/openapi-ts": "^0.78.2",
    "typescript": "^5.3.0"
  }
}
```

## Development

1. **Install dependencies**: `npm install`
2. **Generate code**: `task generate-typescript`
3. **Import types/client** in your application
4. **Configure base URL** and authentication as needed

## Features

- **Modern TypeScript**: Uses latest TypeScript features
- **Tree Shakeable**: Import only what you need
- **Fetch API**: Modern, built-in HTTP client
- **Type Safety**: Full type checking for requests and responses
- **Framework Agnostic**: Works with React, Vue, Angular, Node.js, etc.
- **Zero Runtime Dependencies**: Generated client has minimal dependencies

## Client Configuration

```typescript
import { OpenAPI } from './gen/typescript/client';

// Configure base URL
OpenAPI.BASE = process.env.REACT_APP_API_URL || 'http://localhost:8080';

// Configure authentication
OpenAPI.TOKEN = localStorage.getItem('token') || undefined;

// Configure custom headers
OpenAPI.HEADERS = {
  'X-API-Version': '1.0',
};

// Configure request interceptor
OpenAPI.WITH_CREDENTIALS = true;
``` 