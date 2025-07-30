# /sc:implement - Feature Implementation 🛠️

Intelligent feature and code implementation with auto-activated expertise and comprehensive development support.

## Overview

The `/sc:implement` command creates features, components, and functionality with:
- **Smart Context Detection**: Automatically understands technology stack
- **Expert Activation**: Engages relevant personas (frontend, backend, security)
- **MCP Integration**: Leverages external servers for patterns and UI
- **Quality Built-in**: Includes validation, testing, and best practices

## Syntax

```bash
/sc:implement [feature-description] [options] [flags]
```

### Basic Usage
```bash
/sc:implement "user authentication system"
/sc:implement "responsive navigation component"
/sc:implement "REST API for products"
```

### With Type Specification
```bash
/sc:implement "login form" --type component
/sc:implement "user service" --type service
/sc:implement "payment processing" --type feature
/sc:implement "data models" --type module
```

### With Framework
```bash
/sc:implement "dashboard" --framework react
/sc:implement "API endpoints" --framework express
/sc:implement "mobile app screen" --framework flutter
```

## Arguments & Options

### Feature Description
- Natural language description of what to implement
- Can include specific requirements
- Supports technical specifications

### Implementation Types
- `--type component` - UI components
- `--type api` - API endpoints
- `--type service` - Backend services
- `--type feature` - Full features
- `--type module` - Code modules

### Framework Options
- `--framework react|vue|angular` - Frontend frameworks
- `--framework express|fastapi|django` - Backend frameworks
- `--framework react-native|flutter` - Mobile frameworks

### Quality Options
- `--with-tests` - Include test implementation
- `--documentation` - Generate docs alongside
- `--safe` - Conservative approach
- `--iterative` - Step-by-step validation

## Flag Integration

### Development Flags
```bash
# Include testing
/sc:implement "user feature" --with-tests

# Add documentation
/sc:implement "API" --documentation

# Safe implementation
/sc:implement "payment system" --safe --validate
```

### MCP Server Flags
```bash
# UI components with Magic
/sc:implement "data table" --magic

# Pattern-based with Context7
/sc:implement "auth system" --c7

# Complex logic with Sequential
/sc:implement "workflow engine" --seq
```

### Persona Flags
```bash
# Force specific expertise
/sc:implement "UI component" --persona-frontend
/sc:implement "API security" --persona-security
/sc:implement "microservice" --persona-backend
```

## Auto-Activation Patterns

### Technology Detection
| Keywords | Auto-Activated | MCP Servers |
|----------|---------------|-------------|
| component, UI, responsive | Frontend persona | Magic |
| API, service, endpoint | Backend persona | Context7 |
| auth, security, encryption | Security persona | Sequential |
| database, model, schema | Backend persona | Context7 |

### Complexity-Based Activation
```bash
# Simple component - basic activation
/sc:implement "button component"
# Activates: Frontend persona, Magic

# Complex feature - full activation
/sc:implement "multi-tenant authentication system"
# Activates: Backend, Security personas, Sequential, Context7
```

## Wave Orchestration

Wave mode activates for complex implementations:

```bash
# Automatic wave for complex features
/sc:implement "e-commerce platform" --comprehensive
# Complexity >0.7, multiple components

# Force wave mode
/sc:implement "large feature" --wave-mode force

# Enterprise implementation
/sc:implement "enterprise system" --wave-strategy enterprise
```

### Wave Stages
1. **Analysis**: Understand requirements
2. **Design**: Architecture planning
3. **Implementation**: Code generation
4. **Validation**: Testing and review

## Examples

### Component Implementation
```bash
# Basic React component
/sc:implement "user profile card" --type component --framework react

# Advanced component with tests
/sc:implement "data grid with sorting and filtering" \
  --type component --framework vue --with-tests

# Design system component
/sc:implement "accessible modal dialog" \
  --type component --magic --focus accessibility
```

### API Implementation
```bash
# RESTful API
/sc:implement "CRUD API for products" \
  --type api --framework express

# GraphQL API
/sc:implement "GraphQL resolver for user queries" \
  --type api --framework apollo

# Microservice
/sc:implement "notification microservice" \
  --type service --framework fastapi --with-tests
```

### Feature Implementation
```bash
# Authentication feature
/sc:implement "JWT-based authentication" \
  --type feature --safe --with-tests

# Payment integration
/sc:implement "Stripe payment processing" \
  --type feature --c7 --validate

# Real-time features
/sc:implement "WebSocket chat system" \
  --type feature --framework socket.io
```

### Full-Stack Implementation
```bash
# Complete feature stack
/sc:implement "user dashboard with analytics" \
  --type feature --comprehensive --all-mcp

# Mobile app feature
/sc:implement "offline-first todo app" \
  --type feature --framework react-native

# Enterprise feature
/sc:implement "multi-tenant SaaS billing" \
  --type feature --enterprise --wave-mode
```

## Output Examples

### Component Output
```typescript
// UserProfileCard.tsx
import React from 'react';
import { Card, Avatar, Typography } from '@mui/material';

interface UserProfileCardProps {
  user: {
    name: string;
    email: string;
    avatar?: string;
    role: string;
  };
  onClick?: () => void;
}

export const UserProfileCard: React.FC<UserProfileCardProps> = ({
  user,
  onClick
}) => {
  return (
    <Card
      onClick={onClick}
      sx={{ p: 2, cursor: onClick ? 'pointer' : 'default' }}
    >
      <Avatar src={user.avatar} alt={user.name} />
      <Typography variant="h6">{user.name}</Typography>
      <Typography variant="body2" color="text.secondary">
        {user.email}
      </Typography>
      <Typography variant="caption">{user.role}</Typography>
    </Card>
  );
};

// Tests included when --with-tests
// Documentation generated when --documentation
```

### API Output
```javascript
// productRoutes.js
const express = require('express');
const router = express.Router();
const { authenticate } = require('../middleware/auth');
const ProductController = require('../controllers/productController');

// GET all products
router.get('/products', ProductController.getAll);

// GET single product
router.get('/products/:id', ProductController.getById);

// POST create product (authenticated)
router.post('/products', authenticate, ProductController.create);

// PUT update product (authenticated)
router.put('/products/:id', authenticate, ProductController.update);

// DELETE product (authenticated)
router.delete('/products/:id', authenticate, ProductController.delete);

module.exports = router;
```

## Best Practices

### 1. Clear Specifications
```bash
# GOOD: Specific requirements
/sc:implement "paginated data table with sorting, filtering, and CSV export" \
  --type component --framework react

# BAD: Vague description
/sc:implement "table"
```

### 2. Appropriate Type Selection
```bash
# Component for UI
/sc:implement "navigation menu" --type component

# API for endpoints
/sc:implement "user endpoints" --type api

# Feature for complete functionality
/sc:implement "user management system" --type feature
```

### 3. Framework Consistency
```bash
# Check existing framework
/sc:analyze package.json

# Implement with same framework
/sc:implement "new component" --framework [detected-framework]
```

### 4. Progressive Implementation
```bash
# Start simple
/sc:implement "basic auth" --type feature

# Enhance iteratively
/sc:improve auth --focus security
/sc:implement "2FA for auth" --type enhancement
```

## Performance Considerations

### Token Usage
- Simple component: 5-10K tokens
- API endpoints: 10-15K tokens
- Complex feature: 20-30K tokens
- Wave mode: 40K+ tokens

### Optimization Strategies
```bash
# Specific scope
/sc:implement "login form only" --type component

# Disable unused servers
/sc:implement "backend API" --no-magic

# Use caching
/sc:implement "similar component" --use-cache
```

## Integration Patterns

### With Analysis
```bash
# Analyze first
/sc:analyze existing-code
/sc:implement "enhancement based on analysis"
```

### With Testing
```bash
# Implement with tests
/sc:implement feature --with-tests
/sc:test feature --comprehensive
```

### With Documentation
```bash
# Document while implementing
/sc:implement feature --documentation
/sc:document feature --api-docs
```

## Advanced Features

### Iterative Implementation
```bash
# Step-by-step implementation
/sc:implement "complex feature" --iterative
# Step 1: Core functionality
# Step 2: Edge cases
# Step 3: Optimization
# Step 4: Polish
```

### Template-Based Implementation
```bash
# Use existing patterns
/sc:implement "new service" --template existing-service

# Design system compliance
/sc:implement "component" --design-system material-ui
```

### Multi-Language Support
```bash
# Implement with localization
/sc:implement "user interface" --i18n en,es,fr
```

## Troubleshooting

### Common Issues

#### Wrong Technology Detection
```bash
# Solution: Specify explicitly
/sc:implement feature --framework react --type component
```

#### Missing Dependencies
```bash
# Solution: Check and install
/sc:analyze package.json
/sc:implement feature --check-deps
```

#### Incomplete Implementation
```bash
# Solution: Use iterative mode
/sc:implement complex-feature --iterative --validate
```

## Related Commands

- `/sc:analyze` - Understand before implementing
- `/sc:build` - For project-level construction
- `/sc:improve` - Enhance implementations
- `/sc:test` - Validate implementations
- `/sc:document` - Document implementations

## Quick Reference

### Common Patterns
```bash
# React component
/sc:implement "component" --framework react --with-tests

# REST API
/sc:implement "API" --type api --framework express

# Full feature
/sc:implement "feature" --comprehensive --validate
```

### Power User
```bash
# Maximum intelligence
/sc:implement "complex system" --all-mcp --wave-mode --with-tests --documentation

# Production-ready
/sc:implement "critical feature" --safe --validate --with-tests --persona-security
```

Remember: Clear specifications lead to better implementations!
