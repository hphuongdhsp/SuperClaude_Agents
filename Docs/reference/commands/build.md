# /sc:build - Project Building & Compilation

## Overview
The `/sc:build` command handles project building, compilation, and packaging with intelligent framework detection and optimization. Note: This command focuses on compilation/packaging - use `/sc:implement` for feature implementation.

## Command Syntax
```bash
/sc:build [target] [--type dev|prod|test] [--clean] [--optimize] [--verbose]
```

## Arguments

### Positional Arguments
- `target` - Project, module, or component to build (optional)
  - If omitted, builds the entire project
  - Can be a directory path or project identifier

### Flags
- `--type` - Build configuration type
  - `dev` - Development build with debugging symbols
  - `prod` - Production build with optimizations (default)
  - `test` - Test build with coverage instrumentation
- `--clean` - Clean build artifacts before building
- `--optimize` - Enable advanced build optimizations
- `--verbose` - Show detailed build output
- `--watch` - Enable watch mode for continuous builds
- `--parallel` - Enable parallel compilation where supported

## Features

### Intelligent Framework Detection
- Automatically detects build tools and frameworks
- Supports multiple languages and build systems
- Configures appropriate build commands

### Build Systems Supported
- **JavaScript/TypeScript**: npm, yarn, pnpm, webpack, vite, rollup
- **Python**: setuptools, poetry, pip, conda
- **Java/Kotlin**: gradle, maven, ant
- **Go**: go build, go modules
- **Rust**: cargo
- **C/C++**: make, cmake, bazel
- **.NET**: dotnet CLI, msbuild

### Error Handling
- Comprehensive error detection and reporting
- Automatic dependency resolution attempts
- Clear diagnostic messages with solutions
- Build failure recovery strategies

## Wave Orchestration
This command supports wave orchestration for complex builds:
- **Stage 1**: Environment analysis and validation
- **Stage 2**: Dependency resolution and preparation
- **Stage 3**: Build execution with monitoring
- **Stage 4**: Optimization and packaging

## Examples

### Basic Usage
```bash
# Build entire project
/sc:build

# Build specific module
/sc:build @src/auth

# Production build with optimization
/sc:build --type prod --optimize
```

### Development Workflow
```bash
# Clean development build
/sc:build --type dev --clean

# Watch mode for continuous development
/sc:build --watch --type dev

# Verbose output for debugging
/sc:build --verbose --type dev
```

### Production Deployment
```bash
# Full production build pipeline
/sc:build --type prod --clean --optimize

# Test build before production
/sc:build --type test && /sc:test && /sc:build --type prod
```

### Complex Projects
```bash
# Monorepo with multiple packages
/sc:build @packages/api --type prod
/sc:build @packages/frontend --type prod

# Parallel build for performance
/sc:build --parallel --optimize
```

## Auto-Activated Personas
- **Frontend**: For UI/frontend builds
- **Backend**: For server/API builds
- **DevOps**: For deployment builds
- **Architect**: For complex build configurations

## MCP Server Integration
- **Context7**: Build tool documentation and patterns
- **Sequential**: Complex build orchestration
- **Magic**: UI build optimizations

## Common Build Scenarios

### React/Next.js Application
```bash
/sc:build frontend --type prod --optimize
# Detects: package.json, next.config.js
# Executes: npm run build / yarn build
```

### Python Package
```bash
/sc:build --clean
# Detects: setup.py, pyproject.toml
# Executes: python setup.py build / poetry build
```

### Go Service
```bash
/sc:build cmd/server --type prod --optimize
# Detects: go.mod
# Executes: go build -ldflags="-s -w"
```

### Docker Container
```bash
/sc:build --type prod
# Detects: Dockerfile
# Executes: docker build with optimizations
```

## Performance Characteristics
- **Token Usage**: Medium (5-15K tokens)
- **Execution Time**: Varies by project size (30s - 10m)
- **Complexity**: Moderate to High
- **Wave Support**: Yes (for complex builds)

## Best Practices

### 1. Clean Builds
```bash
# Periodic clean builds prevent issues
/sc:build --clean --type prod
```

### 2. Incremental Development
```bash
# Use watch mode during development
/sc:build --watch --type dev
```

### 3. Build Validation
```bash
# Always test before production build
/sc:build --type test && /sc:test && /sc:build --type prod
```

### 4. Optimization Strategy
```bash
# Optimize only for production
/sc:build --type prod --optimize
```

## Troubleshooting

### Build Failures
- Check error messages for missing dependencies
- Run with `--verbose` for detailed output
- Try `--clean` to resolve cache issues

### Performance Issues
- Enable `--parallel` for multi-core builds
- Use `--optimize` carefully (increases build time)
- Consider incremental builds for large projects

### Environment Issues
- Verify correct Node.js/Python/etc. versions
- Check environment variables
- Ensure build tools are installed

## Integration with Other Commands
```bash
# Complete development cycle
/sc:analyze && /sc:implement feature && /sc:build && /sc:test

# Deployment pipeline
/sc:build --type prod && /sc:test e2e && /sc:git commit
```

## Related Commands
- `/sc:implement` - Feature implementation
- `/sc:test` - Run tests after building
- `/sc:git` - Version control after building
- `/sc:document` - Generate build documentation

## Notes
- Build configuration is cached for performance
- Supports CI/CD pipeline integration
- Respects .gitignore and build ignore files
- Generates build reports in supported frameworks
