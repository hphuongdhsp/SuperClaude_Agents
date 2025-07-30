# SuperClaude Command Reference 📘

Complete reference guide for all SuperClaude `/sc:` commands with examples, use cases, and best practices.

## Command Categories

### 🔍 Analysis & Investigation
- **[/sc:analyze](analyze.md)** - Multi-dimensional code and system analysis
- **[/sc:troubleshoot](troubleshoot.md)** - Problem investigation and debugging
- **[/sc:explain](explain.md)** - Educational explanations and documentation

### 🛠️ Development & Implementation
- **[/sc:build](build.md)** - Project builder with framework detection
- **[/sc:implement](implement.md)** - Feature and code implementation
- **[/sc:design](design.md)** - Design orchestration and architecture

### 🔧 Quality & Enhancement
- **[/sc:improve](improve.md)** - Evidence-based code enhancement
- **[/sc:cleanup](cleanup.md)** - Project cleanup and technical debt reduction
- **[/sc:test](test.md)** - Testing workflows and automation

### 📝 Documentation & Planning
- **[/sc:document](document.md)** - Documentation generation
- **[/sc:estimate](estimate.md)** - Evidence-based project estimation
- **[/sc:workflow](workflow.md)** - Workflow design and optimization

### 🔀 Version Control & Deployment
- **[/sc:git](git.md)** - Git workflow assistant

### 🎯 Meta & Orchestration
- **[/sc:index](index.md)** - Command catalog browsing
- **[/sc:load](load.md)** - Project context loading
- **[/sc:spawn](spawn.md)** - Task orchestration
- **[/sc:task](task.md)** - Long-term project management
- **[/sc:todo](todo.md)** - TODO list reformatting

## Quick Command Lookup

| Command | Primary Use | Wave-Enabled | Auto-Personas |
|---------|-------------|--------------|---------------|
| `/sc:analyze` | Code analysis | ✅ Yes | Analyzer, Architect, Security |
| `/sc:build` | Project building | ✅ Yes | Frontend, Backend, Architect |
| `/sc:cleanup` | Tech debt reduction | ❌ No | Refactorer |
| `/sc:design` | System design | ✅ Yes | Architect, Frontend |
| `/sc:document` | Documentation | ❌ No | Scribe, Mentor |
| `/sc:estimate` | Time estimation | ❌ No | Analyzer, Architect |
| `/sc:explain` | Explanations | ❌ No | Mentor, Scribe |
| `/sc:git` | Version control | ❌ No | DevOps, Scribe, QA |
| `/sc:implement` | Implementation | ✅ Yes | Frontend, Backend, Security |
| `/sc:improve` | Code improvement | ✅ Yes | Refactorer, Performance, QA |
| `/sc:index` | Command browsing | ❌ No | Mentor, Analyzer |
| `/sc:load` | Context loading | ❌ No | Analyzer, Architect |
| `/sc:spawn` | Task orchestration | ❌ No | Analyzer, Architect, DevOps |
| `/sc:task` | Project management | ✅ Yes | Architect, Analyzer |
| `/sc:test` | Testing | ❌ No | QA |
| `/sc:todo` | TODO formatting | ❌ No | Scribe |
| `/sc:troubleshoot` | Debugging | ❌ No | Analyzer, QA |
| `/sc:workflow` | Workflow design | ✅ Yes | Architect, Analyzer |

## Command Syntax

### Basic Structure
```bash
/sc:command [target] [options] [flags]
```

### Common Arguments
- `[target]` - File, directory, or description
- `@<path>` - Specific path reference
- `!<command>` - Command injection
- `--<flags>` - Modifier flags

### Flag Categories
- **Analysis Depth**: `--think`, `--think-hard`, `--ultrathink`
- **MCP Servers**: `--c7`, `--seq`, `--magic`, `--play`
- **Personas**: `--persona-[name]`
- **Optimization**: `--uc`, `--wave-mode`, `--loop`
- **Safety**: `--validate`, `--safe-mode`

## Usage Patterns

### Simple Commands
```bash
/sc:analyze src/
/sc:build frontend
/sc:test unit
```

### With Specific Targets
```bash
/sc:analyze @src/auth --focus security
/sc:implement "user login" --type feature
/sc:improve src/api --focus performance
```

### Advanced with Flags
```bash
/sc:analyze system --think-hard --seq
/sc:build "React app" --c7 --magic
/sc:improve codebase --loop --iterations 3
```

### Wave-Enabled Operations
```bash
/sc:analyze large-system --comprehensive  # Auto-wave
/sc:improve legacy --wave-mode force     # Force wave
/sc:build enterprise --wave-strategy enterprise
```

## Best Practices

### 1. Start with Analysis
```bash
# Always understand before changing
/sc:analyze target/
/sc:implement feature
```

### 2. Use Appropriate Depth
```bash
# Simple task
/sc:explain "function usage"

# Complex task
/sc:analyze architecture --think-hard
```

### 3. Leverage Auto-Activation
```bash
# Let SuperClaude choose tools
/sc:implement "payment system"  # Auto: backend, security personas
```

### 4. Validate Critical Operations
```bash
# Safety for production
/sc:improve production-code --validate --safe-mode
```

## Command Decision Tree

```
What do you want to do?
├── Understand Code
│   ├── Quick overview → /sc:explain
│   ├── Deep analysis → /sc:analyze
│   └── Find issues → /sc:troubleshoot
├── Create/Build
│   ├── New project → /sc:build
│   ├── New feature → /sc:implement
│   └── Architecture → /sc:design
├── Improve Code
│   ├── Quality → /sc:improve
│   ├── Cleanup → /sc:cleanup
│   └── Testing → /sc:test
├── Documentation
│   ├── Generate → /sc:document
│   ├── Explain → /sc:explain
│   └── Estimate → /sc:estimate
└── Project Management
    ├── Version control → /sc:git
    ├── Task tracking → /sc:task
    └── Workflows → /sc:workflow
```

## Performance Characteristics

| Command | Token Usage | Execution Time | Complexity |
|---------|------------|----------------|------------|
| `/sc:explain` | Low (2-5K) | Fast (<30s) | Simple |
| `/sc:analyze` | Medium (5-15K) | Medium (1-3m) | Moderate |
| `/sc:implement` | Medium (10-20K) | Medium (2-5m) | Moderate |
| `/sc:improve` | High (15-30K) | Long (5-10m) | Complex |
| `/sc:build` | High (20-40K) | Long (10-20m) | Complex |

## Advanced Features

### Wave Orchestration
Wave-enabled commands can execute multi-stage operations:
```bash
/sc:analyze system --wave-mode auto
# Stage 1: Initial assessment
# Stage 2: Deep analysis
# Stage 3: Synthesis
# Stage 4: Recommendations
```

### Iterative Operations
Some commands support loops:
```bash
/sc:improve code --loop --iterations 3
# Iteration 1: Initial improvements
# Iteration 2: Refinements
# Iteration 3: Polish
```

### Command Chaining
Commands can be chained for workflows:
```bash
/sc:analyze module && /sc:improve module && /sc:test module
```

## Quick Reference Card

### Most Used Commands
1. `/sc:analyze` - Understand code
2. `/sc:implement` - Create features
3. `/sc:improve` - Enhance code
4. `/sc:test` - Validate changes
5. `/sc:git` - Version control

### Power User Combos
- Analysis + Implementation: `/sc:analyze && /sc:implement`
- Full cycle: `/sc:design && /sc:implement && /sc:test`
- Quality loop: `/sc:improve --loop && /sc:test`

### Emergency Commands
- Quick fix: `/sc:troubleshoot --think`
- Production issue: `/sc:troubleshoot --seq --urgent`
- Security check: `/sc:analyze --focus security --validate`

## Next Steps

1. Explore individual command guides for detailed usage
2. Try the [Best Practices Guide](../../guides/best-practices.md)
3. Learn about [MCP Integration](../../guides/mcp-integration.md)
4. Understand [Persona System](../../personas-guide.md)

Remember: SuperClaude's intelligence means you can start simple and let it guide you to the right tools!
