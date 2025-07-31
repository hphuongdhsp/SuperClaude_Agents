# /sc:todo - TODO List Reformatting & Enhancement

## Overview
The `/sc:todo` command reads, analyzes, and **rewrites** your TODO.md file with improved formatting, clarity, and actionable descriptions. This command is designed to make your task lists more understandable and executable by Claude Code.

⚠️ **IMPORTANT**: This command **modifies your TODO.md file directly** by replacing its contents with an improved version.

## Command Syntax
```bash
/sc:todo [--high] [--low] [--structured] [--actionable] [--commands] [--dry-run] [--backup]
```

## Arguments

### Task Level Flags
- `--high` - Rewrite tasks as high-level strategic objectives
- `--low` - Rewrite tasks as detailed, granular action items

### Formatting Flags
- `--structured` - Apply consistent formatting with categories and priorities
- `--actionable` - Make descriptions specific with file paths and outcomes
- `--context` - Add project context from CLAUDE.md
- `--commands` - Suggest appropriate /sc: commands for each task

### Safety Flags
- `--dry-run` - Preview changes without modifying the file
- `--backup` - Create TODO.md.bak before rewriting

## Features

### Task Analysis
- Parses existing TODO.md structure
- Identifies task categories and priorities
- Understands task relationships
- Extracts implicit context

### Reformatting Capabilities
- **Clarity Enhancement**: Makes vague tasks specific
- **Context Addition**: Adds relevant project information
- **Consistency**: Applies uniform formatting
- **Organization**: Groups related tasks
- **Prioritization**: Adds priority indicators

### Command Suggestions
When using `--commands`, suggests appropriate commands:
- `/sc:implement` for feature tasks
- `/sc:analyze` for investigation tasks
- `/sc:improve` for optimization tasks
- `/sc:test` for testing tasks
- `/sc:document` for documentation tasks

## Examples

### Basic Usage
```bash
# Reformat with default settings
/sc:todo

# Make tasks more actionable
/sc:todo --actionable

# Preview changes first
/sc:todo --actionable --dry-run
```

### Strategic Planning
```bash
# High-level objectives with structure
/sc:todo --high --structured

# Detailed action items with commands
/sc:todo --low --actionable --commands
```

### Safe Reformatting
```bash
# Create backup before rewriting
/sc:todo --structured --backup

# Preview without changes
/sc:todo --actionable --commands --dry-run
```

### Comprehensive Enhancement
```bash
# Full enhancement with all features
/sc:todo --low --structured --actionable --commands --context
```

## Reformatting Examples

### Before (Original TODO.md):
```markdown
- fix auth bug
- add tests
- update docs
- optimize api
```

### After (--actionable --structured --commands):
```markdown
# TODO.md - Project Task List

## 🚨 High Priority

### 1. Fix Authentication Bug
**Task**: Resolve JWT token validation issue in auth middleware
**Files**: `src/middleware/auth.js`, `src/utils/jwt.js`
**Details**:
- Tokens are expiring prematurely (reported in issue #234)
- Need to check token refresh logic
- Verify timezone handling in expiration calculation
**Suggested Command**: `/sc:troubleshoot @src/middleware/auth.js --focus authentication`

### 2. Add Test Coverage
**Task**: Implement unit tests for authentication module
**Files**: `src/middleware/auth.js`, `tests/auth.test.js`
**Details**:
- Current coverage: 45%
- Target coverage: 80%
- Focus on edge cases and error scenarios
**Suggested Command**: `/sc:implement tests for authentication --type unit`

## 📋 Medium Priority

### 3. Update API Documentation
**Task**: Document new authentication endpoints
**Files**: `docs/api.md`, `README.md`
**Details**:
- Document /auth/login, /auth/refresh, /auth/logout
- Include request/response examples
- Add authentication flow diagram
**Suggested Command**: `/sc:document @src/routes/auth --type api`

### 4. Optimize API Performance
**Task**: Improve response times for user queries
**Files**: `src/controllers/user.js`, `src/models/user.js`
**Details**:
- Current response time: 450ms average
- Target: <200ms
- Consider caching and query optimization
**Suggested Command**: `/sc:improve @src/controllers/user.js --type performance`
```

## Execution Process

### 1. File Reading
```
Reading TODO.md...
Found 4 tasks in 15 lines
```

### 2. Analysis
```
Analyzing task structure...
- High priority: 2 tasks
- Medium priority: 2 tasks
- Categories: bug fix, testing, documentation, optimization
```

### 3. Reformatting
```
Applying improvements:
- Adding specific file paths
- Clarifying task descriptions
- Adding context and details
- Suggesting commands
```

### 4. File Writing
```
✅ Successfully rewrote TODO.md
📁 File path: /home/user/project/TODO.md
📝 New file contains 45 lines (expanded from 15)
```

## Best Practices

### 1. Preview First
```bash
# Always preview major changes
/sc:todo --low --structured --dry-run
```

### 2. Create Backups
```bash
# Backup before major reformatting
/sc:todo --structured --actionable --backup
```

### 3. Iterative Enhancement
```bash
# Start simple, add complexity
/sc:todo --structured
/sc:todo --actionable
/sc:todo --commands
```

### 4. Context Integration
```bash
# Use project context for clarity
/sc:todo --context --actionable
```

## Integration with Workflow

### Planning Phase
```bash
# Organize tasks strategically
/sc:todo --high --structured
```

### Execution Phase
```bash
# Get actionable items with commands
/sc:todo --low --actionable --commands
```

### Review Phase
```bash
# Update and reorganize completed tasks
/sc:todo --structured --context
```

## Auto-Activated Personas
- **Scribe**: Primary persona for documentation formatting
- **Architect**: For high-level strategic planning
- **Analyzer**: For task relationship analysis

## MCP Server Integration
- **Context7**: Documentation best practices
- **Sequential**: Complex task analysis

## Performance Characteristics
- **Token Usage**: Low (2-5K tokens)
- **Execution Time**: Fast (< 30s)
- **Complexity**: Low
- **Wave Support**: No

## Troubleshooting

### File Not Found
- Ensure TODO.md exists in current directory
- Specify path: `/sc:todo @/path/to/TODO.md`

### Formatting Issues
- Use `--structured` for consistent formatting
- Check markdown syntax in original file

### Lost Information
- Use `--backup` to preserve original
- Review with `--dry-run` first

## Related Commands
- `/sc:task` - Long-term task management
- `/sc:estimate` - Task estimation
- `/sc:workflow` - Workflow optimization
- `/sc:implement` - Execute tasks

## Notes
- Preserves all original task information
- Enhances without losing context
- Respects existing priority markers
- Maintains markdown compatibility
- Creates more Claude-friendly task descriptions
