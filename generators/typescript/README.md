# TypeScript Code Generator

This directory contains the **Application Layer** toolchain for generating TypeScript adapters from OpenAPI specifications.

## Architecture Role

In OpenAPI Forge's Clean Architecture:
- **Domain Layer** (`api/`): OpenAPI specifications as single source of truth
- **Application Layer** (`generators/typescript/`): **← You are here** - TypeScript-specific toolchain with isolated dependencies
- **Infrastructure Layer** (`adapters/typescript/`): Production-ready generated TypeScript code

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
# Generate TypeScript adapters
task generate-typescript

# Or generate all language adapters
task generate
```

## Generated Adapters

```
adapters/typescript/
├── client/                      # Full client with SDK
│   ├── types.gen.ts            # TypeScript types
│   ├── sdk.gen.ts              # API service methods
│   ├── schemas.gen.ts          # Schema definitions
│   └── index.ts                # Main exports
└── types/                      # Types-only generation
    ├── types.gen.ts            # TypeScript interfaces
    └── index.ts                # Type exports
```

## Implementation Examples

### Using Generated Client

```typescript
import { AuthenticationService, UsersService } from './adapters/typescript/client';
import type { User, UserCreateRequest } from './adapters/typescript/client';

// Configure the client
import { OpenAPI } from './adapters/typescript/client';
OpenAPI.BASE = 'https://api.example.com';
OpenAPI.TOKEN = 'your-auth-token';

// Use the generated client
async function createUser() {
  const newUser: UserCreateRequest = {
    name: "John Doe",
    email: "john@example.com",
    role: "user"
  };

  try {
    const user: User = await UsersService.createUser(newUser);
    console.log('Created user:', user);
  } catch (error) {
    console.error('Failed to create user:', error);
  }
}

// List users
async function listUsers() {
  try {
    const response = await UsersService.getUserList();
    console.log('Users:', response.users);
  } catch (error) {
    console.error('Failed to fetch users:', error);
  }
}

// Authentication
async function authenticate() {
  try {
    const response = await AuthenticationService.authenticateUser({
      email: "john@example.com",
      password: "secret123"
    });
    console.log('Token:', response.token);
  } catch (error) {
    console.error('Authentication failed:', error);
  }
}
```

### Using Types Only

```typescript
import type { User, UserCreateRequest } from './adapters/typescript/types';

// Use types for your own implementations
interface UserRepository {
  create(data: UserCreateRequest): Promise<User>;
  findAll(): Promise<User[]>;
  findById(id: string): Promise<User | null>;
}

class UserService implements UserRepository {
  async create(data: UserCreateRequest): Promise<User> {
    // Your implementation
    return fetch('/api/v1/users', {
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
import { UsersService } from './adapters/typescript/client';
import type { User } from './adapters/typescript/client';

// React example
import { useState, useEffect } from 'react';

function UsersComponent() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    UsersService.getUserList()
      .then(response => setUsers(response.users || []))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {users.map(user => (
        <div key={user.id}>
          <h3>{user.name}</h3>
          <p>Email: {user.email}</p>
          <p>Role: {user.role}</p>
          <p>Status: {user.status}</p>
        </div>
      ))}
    </div>
  );
}
```

## Dependencies

This generator includes its own isolated dependencies:

```json
{
  "name": "@openapi-forge/generators-typescript",
  "dependencies": {
    "@hey-api/openapi-ts": "^0.78.2"
  }
}
```

For your application, add to your `package.json`:

```json
{
  "dependencies": {
    "@hey-api/client-fetch": "^0.2.0"
  },
  "devDependencies": {
    "typescript": "^5.3.0"
  }
}
```

## Development

1. **Install dependencies**: `npm install`
2. **Generate adapters**: `task generate-typescript`
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
import { OpenAPI } from './adapters/typescript/client';

// Configure base URL
OpenAPI.BASE = process.env.REACT_APP_API_URL || 'http://localhost:8080';

// Configure authentication
OpenAPI.TOKEN = localStorage.getItem('token') || undefined;

// Configure interceptors
OpenAPI.interceptors = {
  request: {
    use: (config) => {
      // Add custom headers
      config.headers['X-Custom-Header'] = 'value';
      return config;
    }
  },
  response: {
    use: (response) => {
      // Handle response
      return response;
    }
  }
};
```

## Clean Architecture Benefits

1. **Isolated Dependencies**: TypeScript toolchain dependencies don't pollute other language generators
2. **Adapter Pattern**: Generated code provides clean interfaces for your business logic
3. **Domain Independence**: Business logic remains separate from HTTP concerns
4. **Type Safety**: Compile-time guarantees for API contracts
5. **Framework Agnostic**: Works with any TypeScript/JavaScript framework
6. **Tree Shaking**: Only bundle what you use for optimal performance 