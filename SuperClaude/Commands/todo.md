---
allowed-tools: [Read, Write, Edit, MultiEdit, Glob, TodoWrite]
description: "Reformat and clarify existing TODO.md content for better understanding"
---

# /sc:todo - TODO List Reformatting

## Purpose
Reformat and clarify existing TODO.md content to make it more understandable and actionable for Claude Code, using project context from CLAUDE.md to enhance task descriptions and organization.

## Usage
```
/sc:todo [--high] [--low] [--structured] [--actionable]
```

## Arguments
- `--high` - Reformat tasks as high-level strategic items with broader context
- `--low` - Reformat tasks as detailed, granular action items
- `--structured` - Apply consistent formatting with categories and priorities
- `--actionable` - Make task descriptions more specific and implementable
- `--context` - Add project context from CLAUDE.md to clarify tasks
- `--commands` - Suggest appropriate SuperClaude commands for each task

## Execution
1. Read existing TODO.md to understand current task descriptions
2. Analyze CLAUDE.md to understand project context and conventions
3. Parse and understand the intent behind each task
4. Reformat tasks with clearer language and structure
5. Add context to make tasks more understandable
6. Organize tasks logically with proper formatting
7. Suggest relevant commands for task execution

## Claude Code Integration
- Uses Read to analyze existing TODO.md and CLAUDE.md
- Applies Write/Edit to rewrite TODO.md with improved formatting
- Leverages project context to enhance task descriptions
- Maintains original intent while improving clarity

## Reformatting Approaches
- **High Level**: Transform tasks into strategic objectives with context
- **Low Level**: Break down tasks into specific, actionable steps
- **Structured**: Apply consistent markdown formatting and organization
- **Actionable**: Add specifics like file paths, function names, and clear outcomes

## Examples
```
/sc:todo --high --structured
/sc:todo --low --actionable
/sc:todo --context --commands
/sc:todo --actionable --structured
```

## Benefits
- Makes TODO.md more understandable for Claude Code
- Improves task clarity and actionability
- Adds helpful context from project documentation
- Suggests appropriate commands for task execution
- Maintains consistency in task formatting
