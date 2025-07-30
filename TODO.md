Improved /sc:todo command prompt for better clarity and file writing

The /sc:todo command documentation has been significantly enhanced to ensure Claude Code understands it must write the reformatted content back to the TODO.md file. Key improvements include:

1. **Clear Purpose Statement**: Added prominent warning that the command modifies files directly
2. **Explicit Execution Steps**: Detailed step-by-step instructions emphasizing the Write tool usage
3. **Tool Usage Requirements**: Dedicated section stating Write tool is MANDATORY
4. **Example Behaviors**: Added examples showing expected file writing behavior
5. **Execution Reminder**: Final section specifically for Claude Code emphasizing file writing

The updated prompt now makes it crystal clear that:
- The Write tool MUST be used to save content
- Simply displaying reformatted content is NOT sufficient
- The primary purpose is to UPDATE the file, not just show results
- Success confirmation must include file path and write confirmation

These changes should resolve the issue where Claude Code was only showing reformatted content without actually updating the TODO.md file.
