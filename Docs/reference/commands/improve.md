# /sc:improve - Evidence-Based Code Enhancement

## Overview
The `/sc:improve` command applies systematic, evidence-based improvements to code quality, performance, and maintainability. It supports iterative refinement through the `--loop` flag and wave orchestration for comprehensive improvements.

## Command Syntax
```bash
/sc:improve [target] [--type quality|performance|maintainability|style] [--focus area] [--safe] [--loop] [--iterations n]
```

## Arguments

### Positional Arguments
- `target` - Files, directories, or entire project to improve
  - Can use glob patterns: `*.js`, `src/**/*.py`
  - Defaults to current directory if omitted

### Primary Flags
- `--type` - Specific improvement category
  - `quality` - Code quality and best practices
  - `performance` - Speed and resource optimization
  - `maintainability` - Readability and structure
  - `style` - Code style and formatting
- `--focus` - Specific area of focus
  - `security` - Security vulnerabilities
  - `testing` - Test coverage and quality
  - `documentation` - Inline documentation
  - `architecture` - Structural improvements
- `--safe` - Apply only low-risk improvements
- `--preview` - Show planned improvements without applying

### Iterative Improvement Flags
- `--loop` - Enable iterative improvement mode
- `--iterations` - Number of improvement cycles (default: 3, max: 10)
- `--interactive` - Require approval between iterations
- `--converge` - Stop when improvements plateau

## Features

### Evidence-Based Improvements
- Metrics-driven decision making
- Before/after comparisons
- Risk assessment for each change
- Validation of improvements

### Improvement Categories

#### Code Quality
- Remove code smells
- Eliminate duplication (DRY)
- Improve naming conventions
- Enhance error handling
- Add input validation

#### Performance
- Algorithm optimization
- Memory usage reduction
- Database query optimization
- Caching implementation
- Async/parallel processing

#### Maintainability
- Reduce complexity
- Improve modularity
- Enhance readability
- Standardize patterns
- Add helpful comments

#### Style
- Consistent formatting
- Convention adherence
- Import organization
- File structure
- Naming standards

## Wave Orchestration
This command supports wave orchestration for comprehensive improvements:
- **Wave 1**: Analysis and assessment
- **Wave 2**: Planning and prioritization
- **Wave 3**: Implementation of improvements
- **Wave 4**: Validation and optimization
- **Wave 5**: Documentation and finalization

## Examples

### Basic Usage
```bash
# Improve all code in current directory
/sc:improve

# Improve specific file
/sc:improve @src/utils.js

# Safe improvements only
/sc:improve src/ --safe
```

### Focused Improvements
```bash
# Performance optimization
/sc:improve api/ --type performance

# Security hardening
/sc:improve --focus security

# Code quality with specific focus
/sc:improve src/ --type quality --focus testing
```

### Iterative Refinement
```bash
# Basic iterative improvement (3 cycles)
/sc:improve src/ --loop

# Custom iterations with interaction
/sc:improve --loop --iterations 5 --interactive

# Converge when improvements plateau
/sc:improve module/ --loop --converge
```

### Preview Mode
```bash
# See what would be improved
/sc:improve src/ --preview

# Preview with specific focus
/sc:improve --type performance --preview
```

## Auto-Activated Personas
- **Refactorer**: Primary persona for code improvements
- **Performance**: For optimization-focused improvements
- **Architect**: For structural improvements
- **QA**: For quality and testing improvements
- **Security**: For security-focused enhancements

## MCP Server Integration
- **Sequential**: Complex improvement analysis
- **Context7**: Best practices and patterns
- **Magic**: UI component improvements

## Improvement Strategies

### 1. Comprehensive Review
```bash
# Full codebase improvement
/sc:improve --loop --iterations 3
# Cycle 1: Major issues
# Cycle 2: Refinements
# Cycle 3: Polish
```

### 2. Targeted Enhancement
```bash
# Focus on specific issues
/sc:improve src/ --focus security --safe
```

### 3. Performance Campaign
```bash
# Multi-phase performance improvement
/sc:improve api/ --type performance --wave-mode force
```

### 4. Quality Gate
```bash
# Pre-deployment quality check
/sc:improve --safe --validate
```

## Metrics and Validation

### Quality Metrics
- Cyclomatic complexity reduction
- Code duplication percentage
- Test coverage improvement
- Documentation coverage
- Type safety percentage

### Performance Metrics
- Execution time improvement
- Memory usage reduction
- Database query optimization
- Bundle size reduction
- Load time improvement

### Validation Steps
1. Syntax validation
2. Type checking
3. Test execution
4. Performance benchmarks
5. Security scanning

## Best Practices

### 1. Start Safe
```bash
# Begin with low-risk improvements
/sc:improve --safe --preview
```

### 2. Focus Areas
```bash
# Target specific concerns
/sc:improve --focus security
/sc:improve --focus performance
```

### 3. Iterative Approach
```bash
# Multiple passes for best results
/sc:improve --loop --iterations 3
```

### 4. Validate Changes
```bash
# Always test after improvements
/sc:improve && /sc:test
```

## Common Improvement Patterns

### Code Quality
- Extract methods from long functions
- Replace magic numbers with constants
- Add error handling to critical paths
- Implement proper logging
- Remove dead code

### Performance
- Optimize loops and algorithms
- Implement caching strategies
- Reduce database calls
- Optimize asset loading
- Parallelize operations

### Maintainability
- Break down complex functions
- Create clear module boundaries
- Standardize naming conventions
- Add JSDoc/docstring comments
- Improve file organization

## Performance Characteristics
- **Token Usage**: High (15-30K tokens)
- **Execution Time**: Medium to Long (5-15m)
- **Complexity**: High
- **Wave Support**: Yes

## Integration with Other Commands
```bash
# Analysis before improvement
/sc:analyze --focus quality && /sc:improve

# Test after improvements
/sc:improve src/ && /sc:test

# Document improvements
/sc:improve && /sc:document --update
```

## Related Commands
- `/sc:analyze` - Identify improvement opportunities
- `/sc:cleanup` - Focus on technical debt
- `/sc:test` - Validate improvements
- `/sc:document` - Document changes

## Notes
- Improvements are incremental and reversible
- Each change includes rationale
- Respects existing code style
- Maintains backward compatibility by default
- Generates improvement reports
