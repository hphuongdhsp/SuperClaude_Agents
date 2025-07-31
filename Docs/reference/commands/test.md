# /sc:test - Testing Workflows & Quality Assurance

## Overview
The `/sc:test` command provides comprehensive testing capabilities including test execution, coverage analysis, and quality assurance workflows. It automatically detects testing frameworks and provides intelligent test orchestration.

## Command Syntax
```bash
/sc:test [target] [--type unit|integration|e2e|all] [--coverage] [--watch] [--fix] [--parallel]
```

## Arguments

### Positional Arguments
- `target` - Specific test files, directories, or test names
  - Can use patterns: `*spec.js`, `user*.test.ts`
  - Defaults to all tests if omitted

### Flags
- `--type` - Type of tests to run
  - `unit` - Unit tests only
  - `integration` - Integration tests
  - `e2e` - End-to-end tests
  - `all` - All test types (default)
- `--coverage` - Generate code coverage reports
- `--watch` - Run tests in watch mode
- `--fix` - Attempt to fix failing tests
- `--parallel` - Run tests in parallel
- `--bail` - Stop on first failure
- `--verbose` - Detailed test output
- `--update-snapshots` - Update test snapshots

## Features

### Framework Detection
Automatically detects and configures:
- **JavaScript/TypeScript**: Jest, Mocha, Vitest, Jasmine, Karma
- **Python**: pytest, unittest, nose, tox
- **Java**: JUnit, TestNG, Mockito
- **Go**: go test, testify
- **Rust**: cargo test
- **.NET**: NUnit, xUnit, MSTest
- **Ruby**: RSpec, Minitest

### Test Categories
- **Unit Tests**: Isolated component testing
- **Integration Tests**: Module interaction testing
- **E2E Tests**: Full workflow testing
- **Performance Tests**: Load and stress testing
- **Snapshot Tests**: UI regression testing

### Coverage Analysis
- Line coverage
- Branch coverage
- Function coverage
- Statement coverage
- Coverage trends over time

## Examples

### Basic Testing
```bash
# Run all tests
/sc:test

# Run specific test file
/sc:test @tests/auth.test.js

# Run tests matching pattern
/sc:test user*.test.js
```

### Test Types
```bash
# Unit tests only
/sc:test --type unit

# Integration tests with coverage
/sc:test --type integration --coverage

# E2E tests in verbose mode
/sc:test --type e2e --verbose
```

### Development Workflow
```bash
# Watch mode for TDD
/sc:test --watch

# Fix simple test failures
/sc:test --fix

# Update snapshots
/sc:test --update-snapshots
```

### CI/CD Integration
```bash
# Full test suite with coverage
/sc:test --coverage --bail

# Parallel execution for speed
/sc:test --parallel --type unit

# Generate test reports
/sc:test --coverage --verbose > test-report.txt
```

## Auto-Activated Personas
- **QA**: Primary persona for testing workflows
- **DevOps**: For CI/CD test integration
- **Performance**: For performance testing
- **Security**: For security test scenarios

## MCP Server Integration
- **Playwright**: Browser-based E2E testing
- **Sequential**: Complex test orchestration
- **Context7**: Testing best practices

## Testing Strategies

### 1. Test-Driven Development (TDD)
```bash
# Write test first
/sc:implement test "user authentication"

# Run in watch mode
/sc:test --watch

# Implement feature
/sc:implement "user authentication"
```

### 2. Continuous Testing
```bash
# Pre-commit testing
/sc:test --type unit --bail

# Full test suite before deploy
/sc:test --coverage --parallel
```

### 3. Regression Testing
```bash
# After bug fix
/sc:test @tests/regression --verbose

# Visual regression
/sc:test --type e2e --update-snapshots
```

### 4. Performance Testing
```bash
# Load testing
/sc:test @tests/performance --type integration

# Benchmark tests
/sc:test benchmark/* --verbose
```

## Test Organization

### Recommended Structure
```
project/
├── src/
│   └── components/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── __tests__/        # Alternative
└── *.test.js        # Co-located tests
```

### Test Naming Conventions
- `*.test.js` / `*.spec.js` - Test files
- `test_*.py` - Python tests
- `*_test.go` - Go tests
- `*.test.ts` - TypeScript tests

## Coverage Goals

### Recommended Thresholds
- **Statements**: 80%
- **Branches**: 75%
- **Functions**: 80%
- **Lines**: 80%

### Setting Coverage Requirements
```bash
# Enforce coverage thresholds
/sc:test --coverage --threshold 80
```

## Best Practices

### 1. Start with Unit Tests
```bash
# Fast feedback loop
/sc:test --type unit --watch
```

### 2. Layer Test Types
```bash
# Unit → Integration → E2E
/sc:test --type unit && /sc:test --type integration && /sc:test --type e2e
```

### 3. Maintain Test Health
```bash
# Regular test maintenance
/sc:test --fix --update-snapshots
```

### 4. Monitor Coverage
```bash
# Track coverage trends
/sc:test --coverage --verbose
```

## Common Test Scenarios

### React Component Testing
```bash
/sc:test components/ --update-snapshots
# Uses: Jest + React Testing Library
```

### API Testing
```bash
/sc:test api/ --type integration --verbose
# Uses: Supertest or similar
```

### Browser Testing
```bash
/sc:test e2e/ --type e2e
# Uses: Playwright/Cypress
```

### Python Package Testing
```bash
/sc:test --coverage
# Uses: pytest with coverage
```

## Performance Characteristics
- **Token Usage**: Low to Medium (3-10K)
- **Execution Time**: Varies (10s - 30m)
- **Complexity**: Low to Moderate
- **Wave Support**: No

## Troubleshooting

### Test Failures
- Use `--verbose` for detailed output
- Check test environment setup
- Verify test data and mocks
- Review recent code changes

### Coverage Issues
- Identify uncovered code paths
- Add tests for edge cases
- Check for unreachable code
- Verify coverage configuration

### Performance Problems
- Use `--parallel` for faster execution
- Split large test suites
- Optimize test setup/teardown
- Mock expensive operations

## Integration with Other Commands
```bash
# Development cycle
/sc:implement feature && /sc:test && /sc:build

# Quality pipeline
/sc:improve code && /sc:test --coverage

# Pre-deployment
/sc:test --type all && /sc:build --type prod
```

## Related Commands
- `/sc:implement` - Create code and tests
- `/sc:improve` - Enhance test quality
- `/sc:troubleshoot` - Debug test failures
- `/sc:analyze` - Analyze test coverage

## Notes
- Tests run in isolated environments
- Supports custom test configurations
- Integrates with CI/CD pipelines
- Generates multiple report formats
- Respects test timeouts and retries
