# Custom Commands Developer Guide

This guide explains how to extend SuperClaude by adding your own custom slash commands. Follow these steps to create commands that integrate seamlessly with Claude Code.

## Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Quick Start](#quick-start)
4. [Command Structure](#command-structure)
5. [Step-by-Step Tutorial](#step-by-step-tutorial)
6. [Testing Your Command](#testing-your-command)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

## Overview

SuperClaude commands are defined as Markdown files in the `SuperClaude/Commands/` directory. Each file contains:
- YAML frontmatter with metadata
- Command documentation
- Usage instructions
- Examples

When you reinstall SuperClaude, the framework automatically discovers and registers all `.md` files as commands.

## Prerequisites

- SuperClaude framework installed
- Basic understanding of Markdown and YAML
- Familiarity with Claude Code tools (Read, Write, Edit, etc.)

## Quick Start

1. Create a new `.md` file in `SuperClaude/Commands/`
2. Add required YAML frontmatter
3. Document your command
4. Run `SuperClaude install` to register

Example minimal command:
```markdown
---
allowed-tools: [Read, Grep, Glob]
description: "Summarize folder contents and structure"
---

# /sc:summary - Folder Summary

## Purpose
Generate a concise summary of folder contents and structure.

## Usage
```
/sc:summary @folder [--depth 2]
```
```

## Command Structure

### Required Frontmatter Fields

```yaml
---
allowed-tools: [tool1, tool2, ...]  # List of Claude Code tools
description: "Brief command description"  # One-line summary
---
```

### Available Tools

- **Read**: Read file contents
- **Write**: Create new files
- **Edit**: Modify existing files
- **MultiEdit**: Multiple edits in one operation
- **Bash**: Execute shell commands
- **Grep**: Search for patterns
- **Glob**: Find files by pattern
- **LS**: List directory contents
- **TodoWrite**: Manage task lists
- **Task**: Launch sub-agents
- **WebSearch**: Search the web
- **WebFetch**: Fetch web content
- **NotebookRead**: Read Jupyter notebooks
- **NotebookEdit**: Edit Jupyter notebooks

### Optional Frontmatter Fields

```yaml
---
allowed-tools: [Read, Write, Edit]
description: "Command description"
category: "development"  # Command category
complexity: "moderate"   # simple, moderate, complex
mcp-servers: ["Context7", "Sequential"]  # MCP integration
personas: ["architect", "frontend"]  # Auto-activate personas
wave-enabled: true  # Enable wave orchestration
---
```

## Step-by-Step Tutorial

### Step 1: Choose Your Command Location

- **Core Commands**: `SuperClaude/Commands/` (for framework contributions)
- **Custom Commands**: `SuperClaude/Commands/` (for personal use)

### Step 2: Create Command File

Create a new file with descriptive name:
```bash
touch SuperClaude/Commands/summary.md
```

### Step 3: Add Frontmatter

Start with required metadata:
```yaml
---
allowed-tools: [Read, Grep, Glob, LS]
description: "Generate folder structure summaries with file counts and sizes"
---
```

### Step 4: Document the Command

Add standard sections:

```markdown
# /sc:summary - Folder Summary Generator

## Purpose
Analyze and summarize folder contents, providing insights into structure, 
file types, and code organization.

## Usage
```
/sc:summary @folder [--depth 2] [--include-sizes] [--format tree|list]
```

## Arguments
- `@folder` - Target folder path to analyze
- `--depth` - Maximum directory depth (default: 2)
- `--include-sizes` - Include file sizes in summary
- `--format` - Output format (tree or list)

## Execution
1. Scan folder structure using LS and Glob
2. Analyze file types and distributions
3. Calculate directory sizes if requested
4. Generate formatted summary report
5. Highlight notable patterns or issues

## Examples
```
/sc:summary @src --depth 3 --include-sizes
/sc:summary @. --format tree
/sc:summary @components --depth 1
```
```

### Step 5: Add Advanced Features (Optional)

Include integration patterns:

```markdown
## Claude Code Integration
- Uses LS for directory traversal
- Applies Glob for pattern matching
- Leverages Read for file sampling
- Integrates with TodoWrite for large folder analysis

## Auto-Activation Patterns
- **Analyzer Persona**: Activated for code quality insights
- **Architect Persona**: Activated for structural analysis
- **Sequential MCP**: Used for complex directory structures

## Performance Considerations
- Optimized for folders with <1000 files
- Uses --uc flag automatically for large directories
- Implements caching for repeated analysis
```

### Step 6: Install and Test

```bash
# Reinstall SuperClaude to register new command
python3 -m SuperClaude install

# Test your command
# In Claude Code, type: /sc:summary @src
```

## Testing Your Command

### 1. Validate Syntax
Check your Markdown file for:
- Valid YAML frontmatter
- Correct tool names
- Proper Markdown formatting

### 2. Test Installation
```bash
# Dry run to preview changes
python3 -m SuperClaude install --dry-run

# Actual installation
python3 -m SuperClaude install
```

### 3. Verify in Claude Code
- Open Claude Code
- Type `/sc:` to see command list
- Your command should appear with its description

### 4. Test Execution
Try your command with various arguments:
```
/sc:summary @.
/sc:summary @src --depth 3
/sc:summary @invalid-path  # Test error handling
```

## Best Practices

### 1. Command Naming
- Use descriptive, action-oriented names
- Keep names concise (1-2 words)
- Follow existing patterns (analyze, build, implement)

### 2. Tool Selection
- Only request tools you actually need
- Consider security implications
- Prefer Read over Write when possible

### 3. Documentation Quality
- Provide clear purpose statement
- Include realistic examples
- Document all arguments
- Explain execution flow

### 4. Error Handling
- Anticipate common errors
- Provide helpful error messages
- Include validation steps

### 5. Integration
- Leverage existing personas
- Use MCP servers when beneficial
- Follow SuperClaude patterns

### 6. Performance
- Consider token usage
- Enable --uc for large operations
- Implement progress tracking with TodoWrite

## Troubleshooting

### Command Not Appearing

1. **Check file location**: Must be in `SuperClaude/Commands/` or subdirectories
2. **Validate frontmatter**: YAML must be valid with required fields
3. **Reinstall**: Run `python3 -m SuperClaude install`
4. **Check logs**: Review installation output for errors

### Command Execution Errors

1. **Tool availability**: Ensure all tools in `allowed-tools` are valid
2. **Permission issues**: Check file system permissions
3. **Path problems**: Use absolute paths or proper references

### Common Issues and Solutions

**Issue**: "Command not recognized"
- **Solution**: Ensure file has `.md` extension and valid frontmatter

**Issue**: "Tool not allowed"
- **Solution**: Add required tools to `allowed-tools` list

**Issue**: "Command fails silently"
- **Solution**: Add error handling and validation to execution steps

### Debug Mode

For detailed debugging:
```bash
# Install with verbose output
python3 -m SuperClaude install --verbose

# Check installation diagnostics
python3 -m SuperClaude install --diagnose
```

## Advanced Topics

### Dynamic Tool Selection
Some commands may need different tools based on arguments:
```yaml
---
allowed-tools: [Read, Write, Edit, Grep, Glob, Task]
description: "Adaptive command with dynamic tool usage"
---
```

### MCP Server Integration
Leverage external servers:
```yaml
---
allowed-tools: [Read, Task]
description: "Command with MCP integration"
mcp-servers: ["Context7", "Sequential", "Magic"]
---
```

### Wave Orchestration
Enable for complex multi-stage operations:
```yaml
---
allowed-tools: [Read, Write, Edit, Task]
description: "Complex operation with wave support"
wave-enabled: true
complexity: "complex"
---
```

## Next Steps

1. Start with a simple command
2. Test thoroughly
3. Iterate based on usage
4. Share with the community
5. Consider contributing to core commands

For more details, see:
- [Command Format Specification](./command-format-specification.md)
- [Command Discovery Technical Details](./technical/command-discovery.md)
- [SuperClaude Commands Guide](./commands-guide.md)