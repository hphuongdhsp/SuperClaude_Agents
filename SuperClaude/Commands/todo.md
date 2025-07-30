---
allowed-tools: [Read, Write, Edit, MultiEdit, Glob, TodoWrite]
description: "Rewrite and update TODO.md file with improved formatting and clarity"
---

# /sc:todo - TODO File Rewriting and Improvement

## Purpose
**⚠️ IMPORTANT: This command MODIFIES your TODO.md file directly by REWRITING its contents.**

This command performs the following actions:
1. Reads your existing TODO.md file
2. Analyzes and reformats the content for better clarity
3. **WRITES the improved content back to TODO.md, replacing the original**

The command uses project context from CLAUDE.md to enhance task descriptions and make them more actionable for Claude Code. Your TODO.md file will be permanently updated with the new format.

## Usage
```
/sc:todo [--high] [--low] [--structured] [--actionable]
```

## Arguments
- `--high` - Rewrite tasks as high-level strategic items with broader context
- `--low` - Rewrite tasks as detailed, granular action items
- `--structured` - Apply consistent formatting with categories and priorities
- `--actionable` - Make task descriptions more specific and implementable
- `--context` - Add project context from CLAUDE.md to clarify tasks
- `--commands` - Suggest appropriate SuperClaude commands for each task
- `--dry-run` - Preview changes without modifying the file
- `--backup` - Create a backup of TODO.md before rewriting

## Execution Steps (MUST COMPLETE ALL)
1. **READ**: Use Read tool to load TODO.md content
2. **ANALYZE**: Parse tasks and understand their intent
3. **CONTEXT**: Read CLAUDE.md for project-specific context
4. **REFORMAT**: Create improved version with:
   - Clearer task descriptions
   - Consistent formatting
   - Added context where helpful
   - Logical organization
5. **WRITE**: Use Write tool to save reformatted content to TODO.md
   - This REPLACES the original file content
   - The Write operation is MANDATORY (unless --dry-run)
6. **CONFIRM**: Report successful update with:
   - File path: `/path/to/TODO.md`
   - Status: "✅ TODO.md has been rewritten with improved formatting"
   - Line count of new file

## Claude Code Integration & Tool Usage
**REQUIRED TOOLS AND ACTIONS:**
1. **Read Tool**: Load TODO.md and CLAUDE.md files
2. **Write Tool**: MUST use to save reformatted content
   - The Write tool call is MANDATORY
   - Write directly to the TODO.md file path
   - This OVERWRITES the existing file
3. **File Path Handling**:
   - Input: Read from `TODO.md` or specified path
   - Output: Write to SAME file path (overwrite)
4. **Success Confirmation**:
   ```
   ✅ Successfully rewrote TODO.md
   📁 File path: /path/to/TODO.md
   📝 New file contains X lines
   ```

**CRITICAL**: The Write tool MUST be called to update the file. Simply displaying reformatted content in the response is NOT sufficient.

## File Rewriting Approaches
- **High Level**: Rewrites tasks as strategic objectives with context
- **Low Level**: Rewrites tasks as specific, actionable steps
- **Structured**: Applies consistent markdown formatting and organization
- **Actionable**: Adds specifics like file paths, function names, and clear outcomes

**Note**: All approaches result in the TODO.md file being updated with the new format.

## Examples

### Basic Usage
```
/sc:todo --actionable
```
**Expected Behavior:**
1. Reads TODO.md
2. Reformats tasks to be more actionable
3. **Writes reformatted content back to TODO.md**
4. Reports: "✅ Successfully rewrote TODO.md"

### Combined Flags
```
/sc:todo --high --structured --context
```
**Expected Behavior:**
1. Reads TODO.md and CLAUDE.md
2. Reformats as high-level tasks with project context
3. **Writes new content to TODO.md (overwrites original)**
4. Confirms file update with path and line count

### Preview Mode (No File Changes)
```
/sc:todo --actionable --dry-run
```
**Expected Behavior:**
1. Shows reformatted content in response
2. **Does NOT write to file**
3. Notes: "Preview mode - no files modified"

## Benefits
- Updates TODO.md file with improved formatting
- Makes tasks more understandable and actionable
- Adds helpful context from project documentation
- Suggests appropriate commands for task execution
- Maintains consistency in task formatting
- Provides a permanently improved TODO.md file

## Important Notes
⚠️ **This command modifies your TODO.md file directly**
- The original content will be replaced
- Use `--dry-run` to preview changes first
- Use `--backup` to save original content
- The file path will be shown after successful update

## EXECUTION REMINDER FOR CLAUDE CODE
When executing this command, you MUST:
1. ✅ Use the Write tool to save reformatted content to TODO.md
2. ✅ Report the file path and confirm the write operation
3. ❌ Do NOT just display reformatted content without writing
4. ❌ Do NOT forget to call the Write tool

**The primary purpose is to UPDATE the TODO.md file, not just show reformatted content.**
