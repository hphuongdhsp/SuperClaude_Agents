# SuperClaude Command Format Specification

This document defines the complete specification for SuperClaude command markdown files, including all required and optional fields, validation rules, and examples.

## Table of Contents
1. [File Structure Overview](#file-structure-overview)
2. [YAML Frontmatter Specification](#yaml-frontmatter-specification)
3. [Content Structure](#content-structure)
4. [Validation Rules](#validation-rules)
5. [Example Templates](#example-templates)
6. [Common Errors](#common-errors)

## File Structure Overview

A SuperClaude command file consists of two main parts:

```markdown
---
# YAML frontmatter (metadata)
---

# Markdown content (documentation)
```

### File Requirements
- **Extension**: Must be `.md`
- **Location**: `SuperClaude/Commands/` or subdirectories
- **Encoding**: UTF-8
- **Line endings**: Unix (LF) preferred

## YAML Frontmatter Specification

### Required Fields

#### `allowed-tools`
- **Type**: Array of strings
- **Purpose**: Specifies which Claude Code tools the command can use
- **Format**: `allowed-tools: [tool1, tool2, ...]`
- **Valid values**: See [Available Tools](#available-tools)

```yaml
allowed-tools: [Read, Write, Edit, Grep]
```

#### `description`
- **Type**: String
- **Purpose**: Brief one-line description shown in command lists
- **Format**: `description: "Clear, concise description"`
- **Length**: 100 characters maximum
- **Style**: Action-oriented, present tense

```yaml
description: "Analyze code quality and generate improvement recommendations"
```

### Optional Fields

#### `category`
- **Type**: String
- **Purpose**: Groups related commands
- **Valid values**: 
  - `development`
  - `analysis`
  - `documentation`
  - `testing`
  - `deployment`
  - `utility`
- **Default**: `utility`

```yaml
category: "analysis"
```

#### `complexity`
- **Type**: String
- **Purpose**: Indicates command complexity for routing decisions
- **Valid values**: `simple`, `moderate`, `complex`
- **Default**: `moderate`

```yaml
complexity: "complex"
```

#### `mcp-servers`
- **Type**: Array of strings
- **Purpose**: Specifies MCP servers to activate
- **Valid values**: `Context7`, `Sequential`, `Magic`, `Playwright`
- **Format**: `mcp-servers: ["server1", "server2"]`

```yaml
mcp-servers: ["Context7", "Sequential"]
```

#### `personas`
- **Type**: Array of strings
- **Purpose**: Auto-activates specific personas
- **Valid values**: 
  - `architect`
  - `frontend`
  - `backend`
  - `analyzer`
  - `security`
  - `mentor`
  - `refactorer`
  - `performance`
  - `qa`
  - `devops`
  - `scribe`

```yaml
personas: ["architect", "analyzer"]
```

#### `wave-enabled`
- **Type**: Boolean
- **Purpose**: Enables wave orchestration for complex operations
- **Default**: `false`

```yaml
wave-enabled: true
```

#### `performance-profile`
- **Type**: String
- **Purpose**: Optimization strategy
- **Valid values**: `optimization`, `standard`, `complex`
- **Default**: `standard`

```yaml
performance-profile: "optimization"
```

#### `auto-flags`
- **Type**: Array of strings
- **Purpose**: Automatically applies flags
- **Format**: `auto-flags: ["--flag1", "--flag2"]`

```yaml
auto-flags: ["--uc", "--validate"]
```

#### `min-claude-version`
- **Type**: String
- **Purpose**: Minimum SuperClaude version required
- **Format**: Semantic version (e.g., "3.1.0")

```yaml
min-claude-version: "3.1.0"
```

### Available Tools

Complete list of valid tools for `allowed-tools`:

| Tool | Purpose | Risk Level |
|------|---------|------------|
| `Read` | Read file contents | Low |
| `Write` | Create new files | Medium |
| `Edit` | Modify existing files | Medium |
| `MultiEdit` | Multiple file edits | Medium |
| `Bash` | Execute shell commands | High |
| `Grep` | Search patterns in files | Low |
| `Glob` | Find files by pattern | Low |
| `LS` | List directory contents | Low |
| `TodoWrite` | Manage task lists | Low |
| `Task` | Launch sub-agents | Medium |
| `WebSearch` | Search the web | Low |
| `WebFetch` | Fetch web content | Low |
| `NotebookRead` | Read Jupyter notebooks | Low |
| `NotebookEdit` | Edit Jupyter notebooks | Medium |
| `ExitPlanMode` | Exit planning mode | Low |

## Content Structure

### Required Sections

#### 1. Title
Format: `# /sc:command-name - Brief Description`

```markdown
# /sc:analyze - Code Analysis
```

#### 2. Purpose
Clear explanation of what the command does.

```markdown
## Purpose
Execute comprehensive code analysis across quality, security, performance, and architecture domains.
```

#### 3. Usage
Command syntax with arguments.

```markdown
## Usage
```
/sc:analyze [target] [--focus area] [--depth level]
```
```

#### 4. Arguments
Detailed argument documentation.

```markdown
## Arguments
- `target` - Files, directories, or project to analyze
- `--focus` - Analysis focus area (quality, security, performance, architecture)
- `--depth` - Analysis depth (quick, deep)
```

### Optional Sections

#### Execution
Step-by-step execution flow.

```markdown
## Execution
1. Discover and categorize files
2. Apply analysis techniques
3. Generate findings
4. Create recommendations
5. Present report
```

#### Examples
Practical usage examples.

```markdown
## Examples
```
/sc:analyze @src --focus security
/sc:analyze @. --depth deep
```
```

#### Claude Code Integration
How the command integrates with Claude Code.

```markdown
## Claude Code Integration
- Uses Glob for file discovery
- Leverages Grep for pattern analysis
- Applies Read for code inspection
```

#### Auto-Activation Patterns
When personas or features auto-activate.

```markdown
## Auto-Activation Patterns
- **Security focus**: Activates security persona
- **Large codebase**: Enables --uc flag
- **Complex analysis**: Activates Sequential MCP
```

#### Performance Notes
Performance considerations and optimizations.

```markdown
## Performance Notes
- Optimized for codebases <10K files
- Uses caching for repeated analysis
- Automatically batches operations
```

## Validation Rules

### Frontmatter Validation

1. **Required fields must exist**
   - `allowed-tools` must be non-empty array
   - `description` must be non-empty string

2. **Tool validation**
   - All tools must be from valid tool list
   - No duplicate tools
   - Case-sensitive matching

3. **Field type validation**
   - Arrays must use proper YAML array syntax
   - Booleans must be `true` or `false`
   - Strings with special characters must be quoted

4. **Value validation**
   - `complexity` must be: simple, moderate, or complex
   - `category` must be from valid category list
   - `personas` must contain valid persona names

### Content Validation

1. **Required sections must exist**
   - Title with `/sc:` prefix
   - Purpose section
   - Usage section
   - Arguments section (if command takes arguments)

2. **Formatting requirements**
   - Proper Markdown syntax
   - Code blocks with triple backticks
   - Consistent heading hierarchy

3. **Naming conventions**
   - Command name must match filename (minus .md)
   - Command name should be lowercase
   - Use hyphens for multi-word commands

## Example Templates

### Simple Command Template

```markdown
---
allowed-tools: [Read, Grep]
description: "Simple analysis command"
---

# /sc:simple - Simple Analysis

## Purpose
Perform basic analysis on target files.

## Usage
```
/sc:simple [target]
```

## Arguments
- `target` - File or directory to analyze

## Execution
1. Read target files
2. Perform analysis
3. Return results
```

### Complex Command Template

```markdown
---
allowed-tools: [Read, Write, Edit, Grep, Glob, Task, TodoWrite]
description: "Complex multi-stage operation with AI coordination"
category: "development"
complexity: "complex"
mcp-servers: ["Context7", "Sequential", "Magic"]
personas: ["architect", "frontend", "backend"]
wave-enabled: true
performance-profile: "optimization"
auto-flags: ["--validate", "--think"]
---

# /sc:complex - Complex Operation

## Purpose
Execute sophisticated multi-stage operation with intelligent orchestration.

## Usage
```
/sc:complex [target] [--option value] [--flag]
```

## Arguments
- `target` - Primary target for operation
- `--option` - Configuration option (default: auto)
- `--flag` - Enable special behavior

## Execution
1. Initial assessment and planning
2. Persona activation based on context
3. MCP server coordination
4. Wave orchestration for complex tasks
5. Progressive execution with validation
6. Result aggregation and reporting

## Claude Code Integration
- Leverages Task tool for parallel processing
- Uses TodoWrite for progress tracking
- Coordinates multiple MCP servers
- Implements wave orchestration

## Auto-Activation Patterns
- **Large scope**: Activates wave mode
- **Frontend tasks**: Activates Magic MCP
- **Complex logic**: Activates Sequential
- **Code patterns**: Activates Context7

## Performance Notes
- Automatically enables compression for large operations
- Implements intelligent caching
- Uses parallel processing where possible

## Examples
```
/sc:complex @src --option optimize
/sc:complex @project --flag --option full
```
```

### Utility Command Template

```markdown
---
allowed-tools: [Read, LS, Glob]
description: "Utility for common tasks"
category: "utility"
complexity: "simple"
---

# /sc:utility - Utility Command

## Purpose
Provide quick utility functionality for common tasks.

## Usage
```
/sc:utility [action] [target]
```

## Arguments
- `action` - Action to perform
- `target` - Target for action

## Examples
```
/sc:utility count @src
/sc:utility list @docs
```
```

## Common Errors

### 1. Invalid YAML

**Error**: "YAML parsing error"
```yaml
# Wrong - missing quotes
description: Analyze code quality: security & performance

# Correct
description: "Analyze code quality: security & performance"
```

### 2. Invalid Tool Names

**Error**: "Unknown tool: read"
```yaml
# Wrong - lowercase
allowed-tools: [read, write]

# Correct - exact case
allowed-tools: [Read, Write]
```

### 3. Missing Required Fields

**Error**: "Missing required field: description"
```yaml
# Wrong - missing description
---
allowed-tools: [Read]
---

# Correct
---
allowed-tools: [Read]
description: "Read and analyze files"
---
```

### 4. Invalid Field Types

**Error**: "allowed-tools must be an array"
```yaml
# Wrong - string instead of array
allowed-tools: Read

# Correct
allowed-tools: [Read]
```

### 5. Command Name Mismatch

**Error**: "Command name doesn't match filename"
```markdown
# Wrong - in file analyze.md
# /sc:analysis - Code Analysis

# Correct
# /sc:analyze - Code Analysis
```

## Best Practices

1. **Keep descriptions concise and clear**
2. **List only necessary tools**
3. **Use appropriate complexity level**
4. **Include practical examples**
5. **Document all arguments**
6. **Consider security implications**
7. **Test thoroughly before deployment**
8. **Follow naming conventions**
9. **Provide error handling guidance**
10. **Include performance considerations**

## Version History

- v1.0: Initial specification
- v1.1: Added MCP server support
- v1.2: Added wave orchestration
- v1.3: Added auto-flags and performance profiles

For implementation details, see:
- [Custom Commands Developer Guide](./custom-commands-guide.md)
- [Command Discovery Technical Details](./technical/command-discovery.md)