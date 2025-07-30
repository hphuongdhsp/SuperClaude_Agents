# /sc:analyze - Comprehensive Code Analysis 🔍

Multi-dimensional code and system analysis with intelligent routing and specialized personas.

## Overview

The `/sc:analyze` command performs deep analysis across multiple dimensions:
- **Code Quality**: Maintainability, readability, complexity
- **Security**: Vulnerabilities, best practices, compliance
- **Performance**: Bottlenecks, optimization opportunities
- **Architecture**: Design patterns, structure, scalability

## Syntax

```bash
/sc:analyze [target] [options] [flags]
```

### Basic Usage
```bash
/sc:analyze src/
/sc:analyze @auth-module
/sc:analyze "entire system"
```

### With Focus Areas
```bash
/sc:analyze src/ --focus security
/sc:analyze api/ --focus performance
/sc:analyze system --focus architecture
```

### With Analysis Depth
```bash
/sc:analyze module --think          # Moderate depth
/sc:analyze system --think-hard     # Deep analysis
/sc:analyze critical --ultrathink   # Maximum depth
```

## Arguments & Options

### Target Specification
- `[target]` - File, directory, or system to analyze
- `@<path>` - Specific path reference
- `"description"` - Natural language target description

### Focus Areas
- `--focus quality` - Code quality and maintainability
- `--focus security` - Security vulnerabilities and risks
- `--focus performance` - Performance bottlenecks
- `--focus architecture` - System design and structure

### Analysis Options
- `--depth quick|deep` - Analysis thoroughness
- `--format text|json|report` - Output format
- `--comprehensive` - All focus areas combined
- `--with-metrics` - Include quantitative metrics

## Flag Integration

### Thinking Flags
```bash
# Progressive analysis depth
/sc:analyze small-module              # Quick scan
/sc:analyze medium-module --think     # Thoughtful analysis
/sc:analyze large-system --think-hard # Deep investigation
/sc:analyze critical-system --ultrathink # Maximum depth
```

### MCP Server Flags
```bash
# Sequential for complex analysis
/sc:analyze architecture --seq

# Context7 for pattern detection
/sc:analyze implementation --c7

# Combined for comprehensive analysis
/sc:analyze full-system --seq --c7
```

### Persona Flags
```bash
# Force specific personas
/sc:analyze security-module --persona-security
/sc:analyze ui-components --persona-frontend
/sc:analyze system-design --persona-architect
```

## Auto-Activation Patterns

### Automatic Persona Selection
| Context | Auto-Activated Persona | Reason |
|---------|----------------------|---------|
| Security keywords | Security | Threat analysis |
| Architecture terms | Architect | System design |
| Performance issues | Performance | Optimization |
| UI/Frontend code | Frontend | UX analysis |

### Automatic MCP Activation
| Pattern | Auto-Activated Server | Use Case |
|---------|---------------------|-----------|
| Complex problems | Sequential | Multi-step analysis |
| Library usage | Context7 | Pattern verification |
| --think flags | Sequential | Structured thinking |

## Wave Orchestration

The analyze command supports wave mode for large-scale analysis:

```bash
# Automatic wave activation
/sc:analyze large-codebase --comprehensive
# Triggers when: complexity >0.7, files >20, focus areas >2

# Force wave mode
/sc:analyze system --wave-mode force

# Select wave strategy
/sc:analyze enterprise --wave-strategy systematic
```

### Wave Execution Stages
1. **Discovery**: Map system structure
2. **Analysis**: Deep examination by domain
3. **Synthesis**: Cross-domain insights
4. **Recommendations**: Prioritized actions

## Examples

### Basic Analysis
```bash
# Quick quality check
/sc:analyze src/utils

# Security scan
/sc:analyze auth/ --focus security

# Performance review
/sc:analyze api/ --focus performance --with-metrics
```

### Advanced Analysis
```bash
# Deep architectural review
/sc:analyze @system --focus architecture --think-hard --seq

# Comprehensive security audit
/sc:analyze production/ --focus security --validate --persona-security

# Multi-domain analysis
/sc:analyze app/ --comprehensive --wave-mode auto
```

### Real-World Scenarios
```bash
# Pre-deployment check
/sc:analyze release-branch --comprehensive --validate

# Technical debt assessment
/sc:analyze legacy-module --focus quality --with-metrics

# Performance optimization
/sc:analyze slow-endpoint --focus performance --seq --with-metrics

# Security compliance
/sc:analyze api/ --focus security --validate --safe-mode
```

## Output Examples

### Quality Analysis Output
```
📊 Code Quality Analysis: src/auth

Metrics:
- Complexity: 7.2/10 (Moderate)
- Maintainability: 82/100 (Good)
- Test Coverage: 67% (Needs improvement)

Issues Found:
🔴 High: Complex nested conditions in auth.js:142
🟡 Medium: Duplicate code in validateUser() and checkUser()
🟢 Low: Missing JSDoc comments in 3 functions

Recommendations:
1. Refactor auth.js:142 to reduce complexity
2. Extract common validation logic
3. Add missing documentation
```

### Security Analysis Output
```
🛡️ Security Analysis: api/

Vulnerabilities:
🔴 Critical: SQL injection risk in user.js:87
🔴 High: Missing input validation in payment.js:45
🟡 Medium: Weak password requirements
🟢 Low: Missing security headers

Compliance:
- OWASP Top 10: 3 issues found
- PCI DSS: Payment handling needs review

Immediate Actions:
1. Fix SQL injection vulnerability
2. Add input validation
3. Implement rate limiting
```

## Best Practices

### 1. Start Broad, Then Focus
```bash
# Initial scan
/sc:analyze project/

# Focus on issues
/sc:analyze project/problem-area --focus quality --think
```

### 2. Use Progressive Depth
```bash
# Quick overview
/sc:analyze module

# Detailed investigation
/sc:analyze module --think-hard --with-metrics
```

### 3. Combine with Other Commands
```bash
# Analyze then improve
/sc:analyze code --focus quality
/sc:improve code --based-on-analysis

# Analyze then document
/sc:analyze system --comprehensive
/sc:document system --from-analysis
```

### 4. Regular Analysis Cycles
```bash
# Pre-commit
/sc:analyze changes --quick

# Pre-release
/sc:analyze release --comprehensive --validate

# Periodic health check
/sc:analyze codebase --comprehensive --with-metrics
```

## Performance Considerations

### Token Usage
- Quick scan: 2-5K tokens
- Standard analysis: 5-15K tokens
- Deep analysis: 15-30K tokens
- Wave mode: 30K+ tokens

### Execution Time
- Small module: <1 minute
- Medium project: 2-5 minutes
- Large system: 5-15 minutes
- Enterprise scale: 15-30 minutes

### Optimization Tips
```bash
# Focus specific areas
/sc:analyze api/ --focus performance  # Not --comprehensive

# Use caching
/sc:analyze stable-code --cached

# Disable unneeded servers
/sc:analyze backend --no-magic  # Skip UI server
```

## Troubleshooting

### Common Issues

#### Analysis Too Slow
```bash
# Solution: Narrow scope
/sc:analyze specific-module  # Not entire-project

# Or disable MCP
/sc:analyze module --no-mcp
```

#### Missing Insights
```bash
# Solution: Increase depth
/sc:analyze module --think-hard --comprehensive
```

#### Wrong Focus
```bash
# Solution: Specify focus explicitly
/sc:analyze code --focus security  # Not auto-detect
```

## Integration with Workflow

### Development Cycle
```bash
# 1. Initial analysis
/sc:analyze feature-branch

# 2. Implementation
/sc:implement improvements

# 3. Verification
/sc:analyze feature-branch --compare

# 4. Documentation
/sc:document changes
```

### CI/CD Pipeline
```bash
# Automated quality gate
/sc:analyze src/ --format json --threshold 80

# Security gate
/sc:analyze app/ --focus security --validate --fail-on critical
```

## Advanced Features

### Comparative Analysis
```bash
# Before/after comparison
/sc:analyze module --baseline
# ... make changes ...
/sc:analyze module --compare-baseline
```

### Trend Analysis
```bash
# Track metrics over time
/sc:analyze project --with-metrics --track
```

### Custom Rules
```bash
# Apply custom analysis rules
/sc:analyze code --rules custom-rules.yaml
```

## Related Commands

- `/sc:troubleshoot` - For specific problem investigation
- `/sc:improve` - To act on analysis findings
- `/sc:test` - To validate analysis results
- `/sc:document` - To document findings

## Quick Reference

### Essential Patterns
```bash
/sc:analyze target                    # Basic analysis
/sc:analyze target --focus area       # Specific focus
/sc:analyze target --think-hard       # Deep analysis
/sc:analyze target --comprehensive    # All aspects
```

### Power User
```bash
/sc:analyze system --wave-mode --all-mcp --with-metrics
/sc:analyze critical --ultrathink --validate --safe-mode
```

Remember: Analysis is the foundation - always analyze before making changes!
