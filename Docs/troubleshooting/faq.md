# SuperClaude FAQ - Frequently Asked Questions 🤔

Quick answers to the most common questions about SuperClaude.

## General Questions

### What is SuperClaude?
SuperClaude is a framework that extends Claude Code with specialized commands, AI personas, and external server integrations to enhance development workflows.

### How do I install SuperClaude?
```bash
# From PyPI
uv add SuperClaude

# From source
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
python3 -m SuperClaude install
```

### What's the difference between /sc: commands and regular commands?
- `/sc:` commands are SuperClaude's enhanced commands with intelligent routing
- Regular commands are standard Claude Code operations
- SuperClaude commands include auto-activation, personas, and MCP integration

## Command Questions

### How do I know which command to use?
```bash
# List all commands
/sc:index

# Get help for specific command
/sc:explain analyze

# General guidelines:
# - Understand code: /sc:analyze
# - Create features: /sc:implement
# - Fix issues: /sc:troubleshoot
# - Improve code: /sc:improve
```

### Why aren't my commands working?
Common issues:
1. Missing `/sc:` prefix
2. Typos in command names
3. Invalid arguments
4. Target files don't exist

### Can I create custom commands?
Yes! See the [Custom Commands Guide](../custom-commands-guide.md).

## Persona Questions

### What are personas?
Personas are specialized AI personalities that auto-activate based on context:
- Frontend, Backend, Security, Architect, etc.
- Each has unique priorities and expertise
- 11 personas available

### How do I control which persona activates?
```bash
# Let auto-activation work (recommended)
/sc:implement "UI component"  # Auto: Frontend

# Force specific persona
/sc:analyze code --persona-security

# Disable auto-activation
/sc:analyze code --no-auto-persona
```

### Can multiple personas work together?
Yes! Personas collaborate automatically or manually:
```bash
/sc:analyze system --persona-architect --persona-security
```

## MCP Server Questions

### What are MCP servers?
External servers that provide specialized capabilities:
- **Context7**: Documentation and patterns
- **Sequential**: Complex analysis
- **Magic**: UI generation
- **Playwright**: Testing automation

### When do MCP servers activate?
Automatically based on keywords and context:
```bash
/sc:implement "React component"  # Auto: Context7 + Magic
/sc:troubleshoot "complex bug"   # Auto: Sequential
/sc:test e2e                     # Auto: Playwright
```

### How do I disable MCP servers?
```bash
# Disable all
/sc:analyze code --no-mcp

# Disable specific
/sc:analyze code --no-magic

# Use only specific
/sc:analyze code --only-seq
```

## Performance Questions

### Why is SuperClaude slow?
Common causes:
1. Large scope (analyzing entire project)
2. Multiple MCP servers active
3. Deep analysis flags (--ultrathink)
4. Wave mode on large codebases

Solutions:
```bash
# Narrow scope
/sc:analyze specific-module/

# Disable MCP
/sc:analyze code --no-mcp

# Use compression
/sc:analyze large-project/ --uc
```

### How do I optimize token usage?
```bash
# Auto-compression (>75% usage)
/sc:analyze large-code/  # Auto --uc

# Force compression
/sc:analyze code --uc

# Delegate to sub-agents
/sc:analyze project/ --delegate auto
```

### What is wave mode?
Multi-stage execution for complex operations:
- Auto-activates: complexity >0.7 + files >20
- Progressive analysis and implementation
- Better results for large-scale work

## Troubleshooting Questions

### How do I debug issues?
```bash
# Enable debug mode
/sc:analyze code --debug --verbose

# Check diagnostics
python3 -m SuperClaude diagnose

# Test MCP servers
/sc:test mcp-servers --diagnose
```

### What if a command fails?
1. Check error message
2. Verify target exists
3. Try with --no-mcp
4. Use --safe-mode
5. Check troubleshooting guide

### How do I report bugs?
- GitHub Issues: [Bug reports](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Include: Command used, error message, expected behavior

## Best Practices Questions

### Should I always specify everything?
No! SuperClaude's intelligence works best with minimal configuration:
```bash
# Good - let auto-activation work
/sc:implement "user authentication"

# Over-configured
/sc:implement "user authentication" --persona-backend --c7 --seq --validate
```

### When should I use flags?
Use flags when:
- Auto-activation chooses wrong tools
- You need specific behavior
- Performance optimization needed
- Safety is critical

### What's the best workflow?
```bash
# 1. Analyze first
/sc:analyze feature-area/

# 2. Implement based on analysis
/sc:implement "improvements"

# 3. Test changes
/sc:test feature-area/

# 4. Document
/sc:document changes
```

## Advanced Questions

### What is delegation?
Delegation spawns sub-agents for parallel processing:
```bash
/sc:analyze large-project/ --delegate auto
# Automatically delegates based on size

/sc:analyze project/ --delegate folders
# One sub-agent per folder
```

### How does iterative improvement work?
```bash
/sc:improve code --loop --iterations 3
# Runs 3 improvement cycles
# Each builds on the previous
# Validates between iterations
```

### Can I use SuperClaude in CI/CD?
Yes! Example:
```bash
# Quality gate
/sc:analyze src/ --format json --threshold 80

# Security check
/sc:analyze app/ --focus security --fail-on critical
```

## Quick Tips

### Top 5 Commands
1. `/sc:analyze` - Understand code
2. `/sc:implement` - Create features
3. `/sc:improve` - Enhance code
4. `/sc:test` - Validate changes
5. `/sc:troubleshoot` - Fix issues

### Power User Shortcuts
```bash
# Quick analysis
/sc:analyze .

# Safe implementation
/sc:implement feature --safe

# Fast improvement
/sc:improve code --no-mcp --uc

# Comprehensive test
/sc:test all --comprehensive
```

### Common Gotchas
1. Forgetting `/sc:` prefix
2. Using relative paths with ../
3. Over-specifying flags
4. Fighting auto-activation
5. Not reading error messages

Remember: SuperClaude is designed to be intelligent - trust it!
