# SuperClaude Best Practices Guide 🌟

Master the art of leveraging SuperClaude's full potential with these proven patterns and strategies.

## Table of Contents

1. [Core Philosophy](#core-philosophy)
2. [Command Usage Patterns](#command-usage-patterns)
3. [Persona Optimization](#persona-optimization)
4. [MCP Server Strategies](#mcp-server-strategies)
5. [Token Management](#token-management)
6. [Wave Orchestration](#wave-orchestration)
7. [Security Best Practices](#security-best-practices)
8. [Workflow Optimization](#workflow-optimization)
9. [Common Patterns](#common-patterns)
10. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

## Core Philosophy

### 🎯 The SuperClaude Way

1. **Start Simple, Scale Smart**
   - Begin with basic commands
   - Let auto-activation guide you
   - Add complexity only when needed

2. **Trust the Intelligence**
   - SuperClaude's orchestrator understands context
   - Auto-activation usually picks the right tools
   - Manual overrides are the exception, not the rule

3. **Evidence Over Assumptions**
   - Always verify with `/sc:analyze` first
   - Use `/sc:test` to validate changes
   - Document decisions with `/sc:document`

## Command Usage Patterns

### 🎯 When to Use Each Command

#### Analysis Commands
```bash
# GOOD: Start with analysis before making changes
/sc:analyze src/ --comprehensive
/sc:troubleshoot "performance issues" --think-hard

# BETTER: Use specific focus areas
/sc:analyze src/ --focus security
/sc:analyze src/ --focus performance --with-metrics
```

#### Implementation Commands
```bash
# GOOD: Clear, specific implementations
/sc:implement "user authentication" --type feature --with-tests

# BETTER: Provide framework context
/sc:implement "REST API for user management" --framework express --type api --safe
```

#### Improvement Commands
```bash
# GOOD: Targeted improvements
/sc:improve src/auth --focus security

# BETTER: Iterative improvement with validation
/sc:improve src/auth --focus security --loop --iterations 3
```

### 📊 Command Selection Matrix

| Task Type | Primary Command | Secondary Options | Best Flags |
|-----------|----------------|-------------------|------------|
| New Feature | `/sc:implement` | `/sc:build` | `--with-tests --safe` |
| Bug Fix | `/sc:troubleshoot` | `/sc:analyze` | `--think --seq` |
| Optimization | `/sc:improve` | `/sc:analyze` | `--focus performance --loop` |
| Documentation | `/sc:document` | `/sc:explain` | `--comprehensive --context` |
| Code Review | `/sc:analyze` | `/sc:improve` | `--focus quality --validate` |

## Persona Optimization

### 🎭 Leveraging Auto-Activation

#### Let Context Drive Personas
```bash
# Frontend work auto-activates frontend persona
/sc:implement "responsive navigation component"

# Security work auto-activates security persona
/sc:analyze auth/ --focus security

# Complex debugging auto-activates analyzer
/sc:troubleshoot "memory leak in production"
```

#### Manual Override When Needed
```bash
# Force specific persona for specialized needs
/sc:implement api --persona-backend --focus reliability

# Combine personas for cross-domain work
/sc:analyze system --persona-architect --persona-security
```

### 📈 Persona Effectiveness Guide

| Scenario | Auto-Activated Persona | When to Override |
|----------|----------------------|------------------|
| UI Components | Frontend | Add `--persona-performance` for optimization |
| API Development | Backend | Add `--persona-security` for sensitive data |
| System Design | Architect | Add `--persona-performance` for scalability |
| Bug Investigation | Analyzer | Add domain-specific persona for context |
| Code Cleanup | Refactorer | Add `--persona-qa` for test coverage |

## MCP Server Strategies

### 🔌 Optimal Server Selection

#### Context7 (Documentation & Patterns)
```bash
# Best for framework-specific implementations
/sc:implement "React hooks" --c7
/sc:build "Django REST API" --c7

# Automatic activation for library work
/sc:implement "Stripe payment integration"  # Auto-activates Context7
```

#### Sequential (Complex Analysis)
```bash
# Best for multi-step problems
/sc:analyze architecture --think-hard  # Auto-activates Sequential
/sc:troubleshoot "distributed system issue" --seq

# Combines well with analyzer persona
/sc:analyze codebase --comprehensive --seq
```

#### Magic (UI Generation)
```bash
# Best for component creation
/sc:implement "dashboard component" --magic
/sc:build "responsive layout" --type component

# Auto-activates for UI keywords
/sc:implement "modal with animations"  # Auto-activates Magic
```

#### Playwright (Testing & Automation)
```bash
# Best for E2E testing
/sc:test e2e --play
/sc:test "user workflows" --type integration

# Performance validation
/sc:analyze performance --play --with-metrics
```

### 🎯 Server Coordination Patterns

```bash
# Multi-server for comprehensive solutions
/sc:implement "full-stack feature" --all-mcp

# Selective server usage for efficiency
/sc:build api --seq --c7  # Analysis + documentation

# Disable servers for speed
/sc:analyze small-file.js --no-mcp  # Faster for simple tasks
```

## Token Management

### 💎 Efficient Token Usage

#### Automatic Compression
```bash
# SuperClaude auto-compresses when needed
/sc:analyze large-codebase/  # Auto-activates --uc at >75% tokens

# Force compression for large operations
/sc:analyze entire-project/ --uc
```

#### Progressive Complexity
```bash
# Start simple
/sc:analyze module/

# Add detail progressively
/sc:analyze module/ --think

# Maximum analysis when needed
/sc:analyze module/ --ultrathink
```

### 📊 Token Optimization Strategies

| Operation | Token Strategy | Flags to Use |
|-----------|---------------|--------------|
| Large Codebase | Force compression | `--uc` |
| Multi-file Analysis | Delegate to sub-agents | `--delegate auto` |
| Complex Problems | Progressive depth | Start simple, add `--think` |
| Documentation | Structured output | `--structured --uc` |

## Wave Orchestration

### 🌊 Understanding Wave Mode

Wave orchestration activates automatically for complex multi-domain operations:

```bash
# Automatic wave activation
/sc:improve large-system/ --comprehensive  # Complexity >0.7, files >20

# Force wave mode for borderline cases
/sc:analyze complex-module/ --wave-mode force

# Select wave strategy
/sc:improve legacy-system/ --wave-strategy enterprise
```

### 📈 Wave Strategy Selection

| Scenario | Best Strategy | Example |
|----------|--------------|---------|
| Incremental Improvements | Progressive | `/sc:improve ui/ --wave-strategy progressive` |
| System Analysis | Systematic | `/sc:analyze arch/ --wave-strategy systematic` |
| Large Refactoring | Adaptive | `/sc:improve all/ --wave-strategy adaptive` |
| Enterprise Scale | Enterprise | `/sc:analyze monorepo/ --wave-strategy enterprise` |

## Security Best Practices

### 🔒 Secure Development Patterns

#### Path Security
```bash
# GOOD: Absolute paths
/sc:analyze /home/user/project/src/

# BAD: Relative paths that could escape
/sc:analyze ../../../etc/  # Blocked by framework
```

#### Validation First
```bash
# Always validate before production changes
/sc:implement feature --validate
/sc:improve production-code --safe-mode

# Security-focused analysis
/sc:analyze api/ --focus security --validate
```

### 🛡️ Security Checklist

- ✅ Use `--validate` for critical operations
- ✅ Enable `--safe-mode` in production environments
- ✅ Run security analysis before deployment
- ✅ Use `--persona-security` for sensitive features
- ✅ Document security decisions

## Workflow Optimization

### 🚀 Efficient Development Workflows

#### Feature Development Flow
```bash
# 1. Analyze existing code
/sc:analyze feature-area/ --comprehensive

# 2. Design the solution
/sc:design "new feature" --type feature

# 3. Implement with tests
/sc:implement "feature" --with-tests --safe

# 4. Validate and improve
/sc:test feature/ --comprehensive
/sc:improve feature/ --loop
```

#### Bug Fixing Flow
```bash
# 1. Investigate the issue
/sc:troubleshoot "bug description" --think

# 2. Analyze affected code
/sc:analyze affected-module/ --focus quality

# 3. Implement fix
/sc:implement "bug fix" --type fix --validate

# 4. Test thoroughly
/sc:test affected-areas/ --regression
```

#### Optimization Flow
```bash
# 1. Measure current performance
/sc:analyze app/ --focus performance --with-metrics

# 2. Identify bottlenecks
/sc:troubleshoot "performance issues" --seq

# 3. Iterative improvement
/sc:improve bottlenecks/ --focus performance --loop

# 4. Validate improvements
/sc:test performance --benchmark
```

## Common Patterns

### ✨ Proven Success Patterns

#### The Analysis-First Pattern
```bash
# Always understand before changing
/sc:analyze target/ && /sc:implement changes
```

#### The Progressive Enhancement Pattern
```bash
# Start simple, add complexity
/sc:build feature
/sc:improve feature --focus quality
/sc:improve feature --focus performance
/sc:test feature --comprehensive
```

#### The Documentation-Driven Pattern
```bash
# Document while developing
/sc:implement feature --documentation
/sc:document feature/ --comprehensive
```

#### The Iterative Quality Pattern
```bash
# Continuous improvement cycles
/sc:improve module/ --loop --iterations 3 --validate
```

## Anti-Patterns to Avoid

### ❌ Common Mistakes

#### 1. Skipping Analysis
```bash
# BAD: Jumping straight to implementation
/sc:implement "complex feature"

# GOOD: Analyze first
/sc:analyze related-code/ && /sc:implement "complex feature"
```

#### 2. Over-Engineering
```bash
# BAD: Using all flags unnecessarily
/sc:analyze simple.js --ultrathink --all-mcp --wave-mode force

# GOOD: Let auto-activation work
/sc:analyze simple.js
```

#### 3. Ignoring Validation
```bash
# BAD: No validation for critical changes
/sc:improve security-module/

# GOOD: Always validate security changes
/sc:improve security-module/ --validate --safe-mode
```

#### 4. Manual Everything
```bash
# BAD: Overriding all auto-detection
/sc:analyze code/ --no-mcp --persona-architect --wave-mode off

# GOOD: Trust the framework
/sc:analyze code/
```

## 🎯 Quick Reference Card

### Essential Commands
- **Analyze First**: `/sc:analyze [target]`
- **Implement Safely**: `/sc:implement [feature] --with-tests`
- **Improve Iteratively**: `/sc:improve [target] --loop`
- **Document Always**: `/sc:document [target]`

### Power User Flags
- **Deep Analysis**: `--think-hard` or `--ultrathink`
- **Token Efficiency**: `--uc` (auto-activates >75%)
- **Safety First**: `--validate --safe-mode`
- **Quality Focus**: `--loop --iterations 3`

### Framework Trust
- Let auto-activation work
- Override only when necessary
- Start simple, scale as needed
- Validate critical operations

## 🚀 Next Steps

1. Practice the basic workflow patterns
2. Experiment with auto-activation
3. Learn when to override defaults
4. Build your own patterns

Remember: **SuperClaude is intelligent** - trust it to help you, and it will!
