# SuperClaude Command Development Toolkit

This directory contains tools and templates to help developers create custom SuperClaude commands quickly and correctly.

## Quick Start

### Using the Command Generator

The easiest way to create a new command is using the interactive generator:

```bash
cd SuperClaude_Agents
python3 templates/create-command.py
```

This will walk you through creating a properly formatted command file with all required fields.

### Manual Template Usage

If you prefer to work from a template manually:

1. Copy `command-template.md` to your custom commands directory
2. Replace all `{PLACEHOLDER}` values with your content
3. Save with your command name (e.g., `my-analyzer.md`)

## Available Tools

### 1. Command Generator (`create-command.py`)

Interactive Python script that:
- Prompts for all required information
- Validates inputs (command names, tools, etc.)
- Generates properly formatted command files
- Provides next-step guidance

**Features:**
- Command name validation
- Tool selection with validation
- Category and complexity selection
- Multi-line input for detailed sections
- Automatic file generation

### 2. Command Template (`command-template.md`)

A comprehensive template with all standard sections:
- YAML frontmatter with all fields
- Standard documentation sections
- Placeholders for easy replacement
- Comments explaining each section

## Command Validation Checklist

Before finalizing your command, verify:

### ✅ Metadata
- [ ] Valid YAML frontmatter syntax
- [ ] `allowed-tools` contains only valid tool names
- [ ] `description` is under 100 characters
- [ ] `category` is from allowed list
- [ ] `complexity` is simple/moderate/complex

### ✅ Documentation
- [ ] Clear purpose statement
- [ ] Complete usage syntax
- [ ] All arguments documented
- [ ] Step-by-step execution flow
- [ ] At least 2 practical examples

### ✅ Best Practices
- [ ] Command name is lowercase with hyphens
- [ ] Only requested necessary tools
- [ ] Included error handling section
- [ ] Considered performance implications
- [ ] Added integration notes

## Example Workflow

1. **Generate Command**
   ```bash
   python3 templates/create-command.py
   
   # Follow prompts:
   Command name: analyze-imports
   Brief title: Import Analyzer
   Description: Analyze and optimize project imports
   Category: analysis
   Tools: Read,Grep,Glob
   ```

2. **Review Generated File**
   ```bash
   cat SuperClaude/Commands/custom/analyze-imports.md
   ```

3. **Edit and Enhance**
   - Add more detailed examples
   - Expand execution steps
   - Include edge cases

4. **Test Installation**
   ```bash
   SuperClaude install --dry-run
   ```

5. **Install and Use**
   ```bash
   SuperClaude install
   # In Claude Code: /sc:analyze-imports @src
   ```

## Advanced Templates

### Simple Command Template
For basic single-purpose commands:
```yaml
---
allowed-tools: [Read, Grep]
description: "Simple analysis tool"
---

# /sc:simple - Simple Tool

## Purpose
Quick analysis of target files.

## Usage
```
/sc:simple [target]
```

## Examples
```
/sc:simple @src
```
```

### Complex Command Template
For multi-stage operations:
```yaml
---
allowed-tools: [Read, Write, Edit, Task, TodoWrite]
description: "Complex multi-stage operation"
category: "development"
complexity: "complex"
mcp-servers: ["Context7", "Sequential"]
personas: ["architect", "analyzer"]
wave-enabled: true
---

# /sc:complex - Complex Operation

[Full template with all sections...]
```

## Tips for Success

1. **Start Simple**: Begin with minimal required fields
2. **Test Early**: Install and test basic functionality first
3. **Iterate**: Add features incrementally
4. **Document Well**: Clear examples are crucial
5. **Consider Users**: Write for developers who haven't seen your code

## Common Patterns

### Analysis Commands
```yaml
allowed-tools: [Read, Grep, Glob, LS]
category: "analysis"
personas: ["analyzer"]
```

### Generation Commands
```yaml
allowed-tools: [Write, Read, Edit]
category: "development"
personas: ["frontend", "backend"]
```

### Utility Commands
```yaml
allowed-tools: [Read, LS, Glob]
category: "utility"
complexity: "simple"
```

## Troubleshooting

### Generator Issues

**"Command name must be lowercase with hyphens only"**
- Use: `analyze-deps` ✓
- Not: `AnalyzeDeps` ✗

**"Invalid tools"**
- Check spelling and case (tools are case-sensitive)
- Use exact names from available tools list

### Template Issues

**Placeholders not replaced**
- Ensure you replaced all `{PLACEHOLDER}` text
- Check for typos in placeholder names

**YAML parsing errors**
- Validate YAML syntax (proper indentation)
- Quote strings with special characters

## Future Enhancements

Planned improvements for the toolkit:
- Validation script for command files
- Unit test generator for commands
- Performance profiling tools
- Command packaging for distribution
- Visual command builder

## Contributing

To improve the toolkit:
1. Test thoroughly with various command types
2. Add new templates for specific use cases
3. Enhance validation in the generator
4. Submit pull requests with improvements

## Resources

- [Custom Commands Developer Guide](../Docs/custom-commands-guide.md)
- [Command Format Specification](../Docs/command-format-specification.md)
- [Example Command](../SuperClaude/Commands/custom/summary.md)

---

*Start building your custom commands today!*