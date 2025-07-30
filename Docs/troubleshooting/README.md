# SuperClaude Troubleshooting Guide 🔧

Quick solutions to common issues and problems with SuperClaude.

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [Command Execution Problems](#command-execution-problems)
3. [Performance Issues](#performance-issues)
4. [MCP Server Issues](#mcp-server-issues)
5. [Persona & Auto-Activation Issues](#persona--auto-activation-issues)
6. [Token & Resource Issues](#token--resource-issues)
7. [Integration Issues](#integration-issues)
8. [Common Error Messages](#common-error-messages)
9. [Quick Fixes](#quick-fixes)
10. [Getting Help](#getting-help)

## Installation Issues

### SuperClaude Command Not Found

**Problem**: After installation, `/sc:` commands aren't recognized.

**Solutions**:
```bash
# 1. Verify installation
python3 -m SuperClaude install --diagnose

# 2. Check installation path
ls ~/.claude/

# 3. Reinstall if needed
python3 -m SuperClaude install --force

# 4. Manual installation
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
python3 -m SuperClaude install
```

### Permission Denied Errors

**Problem**: Installation fails with permission errors.

**Solutions**:
```bash
# 1. Install to user directory (recommended)
python3 -m SuperClaude install --user

# 2. Check directory permissions
ls -la ~/.claude/

# 3. Fix permissions if needed
chmod 755 ~/.claude/
```

### Missing Dependencies

**Problem**: Import errors or missing packages.

**Solutions**:
```bash
# 1. Install with uv (recommended)
uv add SuperClaude

# 2. Install dependencies manually
pip install -r requirements.txt

# 3. Use virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install SuperClaude
```

## Command Execution Problems

### Command Not Recognized

**Problem**: `/sc:command` returns "command not found".

**Solutions**:
```bash
# 1. Check command exists
/sc:index  # List all available commands

# 2. Verify correct syntax
/sc:analyze  # Correct
/analyze     # Incorrect (missing sc: prefix)

# 3. Check for typos
/sc:implement  # Correct
/sc:impliment  # Incorrect spelling
```

### Commands Failing Silently

**Problem**: Commands run but produce no output or errors.

**Solutions**:
```bash
# 1. Enable verbose mode
/sc:analyze src/ --verbose

# 2. Check for path issues
/sc:analyze /absolute/path/to/src/  # Use absolute paths

# 3. Validate target exists
ls src/  # Verify directory exists
/sc:analyze src/
```

### Unexpected Command Behavior

**Problem**: Commands don't work as expected.

**Solutions**:
```bash
# 1. Check command documentation
/sc:explain analyze  # Get command help

# 2. Use correct arguments
/sc:implement "feature" --type component  # Correct
/sc:implement --type component "feature"  # May not work

# 3. Reset to defaults
/sc:analyze src/  # Let auto-activation work
```

## Performance Issues

### Slow Command Execution

**Problem**: Commands take too long to execute.

**Solutions**:
```bash
# 1. Narrow scope
/sc:analyze specific-module/  # Not entire-project/

# 2. Disable MCP servers
/sc:analyze src/ --no-mcp  # 40-60% faster

# 3. Use compression
/sc:analyze large-project/ --uc  # Reduce token usage

# 4. Skip wave mode
/sc:analyze project/ --wave-mode off
```

### High Memory/CPU Usage

**Problem**: SuperClaude consumes too many resources.

**Solutions**:
```bash
# 1. Limit concurrent operations
/sc:analyze src/ --concurrency 3  # Default is 7

# 2. Use safe mode
/sc:improve code --safe-mode  # Conservative resource usage

# 3. Process in batches
/sc:analyze src/module1/
/sc:analyze src/module2/  # Instead of src/ all at once
```

### Token Limit Exceeded

**Problem**: Operations fail due to token limits.

**Solutions**:
```bash
# 1. Force compression
/sc:analyze project/ --uc

# 2. Use delegation
/sc:analyze large-project/ --delegate auto

# 3. Reduce analysis depth
/sc:analyze project/  # Instead of --ultrathink

# 4. Focus specific areas
/sc:analyze project/ --focus security  # Not --comprehensive
```

## MCP Server Issues

### Server Connection Failed

**Problem**: MCP servers fail to connect or timeout.

**Solutions**:
```bash
# 1. Disable problematic server
/sc:analyze code --no-seq  # If Sequential fails

# 2. Increase timeout
/sc:implement feature --timeout 60

# 3. Use fallback mode
/sc:implement feature --no-mcp  # Use native tools only

# 4. Check server status
/sc:test mcp-servers --diagnose
```

### Wrong Server Activation

**Problem**: Inappropriate MCP server activates.

**Solutions**:
```bash
# 1. Disable auto-activation
/sc:analyze backend --no-magic  # Disable UI server

# 2. Force specific servers
/sc:implement feature --only-c7  # Only Context7

# 3. Manual server selection
/sc:analyze code --seq --no-auto  # Manual Sequential
```

### Server Response Errors

**Problem**: MCP servers return errors or invalid responses.

**Solutions**:
```bash
# 1. Clear server cache
/sc:analyze code --clear-cache

# 2. Force refresh
/sc:implement feature --c7 --refresh

# 3. Try alternative server
/sc:implement UI --magic  # If Context7 fails for UI
```

## Persona & Auto-Activation Issues

### Wrong Persona Activated

**Problem**: Incorrect persona activates for the task.

**Solutions**:
```bash
# 1. Override auto-activation
/sc:implement API --persona-backend  # Force backend

# 2. Disable auto-activation
/sc:analyze code --no-auto-persona

# 3. Combine personas
/sc:analyze system --persona-architect --persona-security
```

### Persona Not Activating

**Problem**: Expected persona doesn't activate.

**Solutions**:
```bash
# 1. Use explicit activation
/sc:analyze security-code --persona-security

# 2. Check activation keywords
/sc:implement "security feature"  # Should activate security

# 3. Force activation
/sc:analyze code --force-persona frontend
```

## Token & Resource Issues

### Context Length Exceeded

**Problem**: Operation fails due to context limits.

**Solutions**:
```bash
# 1. Enable ultra-compression
/sc:analyze large-code --uc

# 2. Use delegation
/sc:analyze project/ --delegate folders

# 3. Process incrementally
/sc:analyze project/part1/
/sc:analyze project/part2/

# 4. Reduce scope
/sc:analyze critical-files-only/
```

### Resource Exhaustion

**Problem**: System runs out of memory or CPU.

**Solutions**:
```bash
# 1. Enable safe mode
/sc:improve large-project --safe-mode

# 2. Limit concurrency
/sc:analyze project/ --concurrency 1

# 3. Use minimal flags
/sc:analyze project/  # No --comprehensive or --all-mcp

# 4. Monitor resources
/sc:analyze project/ --monitor-resources
```

## Integration Issues

### Claude Code Integration Problems

**Problem**: SuperClaude doesn't integrate properly with Claude Code.

**Solutions**:
```bash
# 1. Verify Claude Code version
# Ensure using claude.ai/code

# 2. Check installation location
ls ~/.claude/  # Should contain framework files

# 3. Reinstall integration
python3 -m SuperClaude install --integration-only

# 4. Test basic command
/sc:index  # Should list commands
```

### Git Integration Issues

**Problem**: Git commands fail or produce errors.

**Solutions**:
```bash
# 1. Check git configuration
git config --list

# 2. Ensure in git repository
git status

# 3. Use explicit paths
/sc:git commit -m "message"  # From repo root

# 4. Check permissions
ls -la .git/
```

## Common Error Messages

### "File not found"
```bash
# Solution: Use absolute paths
/sc:analyze /home/user/project/src/
```

### "Permission denied"
```bash
# Solution: Check file permissions
chmod 644 file.py
/sc:analyze file.py
```

### "Token limit exceeded"
```bash
# Solution: Enable compression
/sc:analyze project/ --uc
```

### "MCP server timeout"
```bash
# Solution: Disable or increase timeout
/sc:implement feature --no-mcp
# or
/sc:implement feature --timeout 120
```

### "Invalid command syntax"
```bash
# Solution: Check command format
/sc:analyze target --flag  # Correct
/sc:analyze --flag target  # May not work
```

## Quick Fixes

### Reset Everything
```bash
# Clear all caches and reset
/sc:analyze project/ --reset --clear-cache

# Reinstall if needed
python3 -m SuperClaude uninstall
python3 -m SuperClaude install
```

### Performance Quick Fix
```bash
# Fastest analysis mode
/sc:analyze code --no-mcp --uc --no-wave
```

### Safety Quick Fix
```bash
# Maximum safety mode
/sc:implement feature --safe-mode --validate --with-tests
```

### Debug Mode
```bash
# Enable all debugging
/sc:analyze code --debug --verbose --introspect
```

## Getting Help

### Built-in Help
```bash
# List all commands
/sc:index

# Explain specific command
/sc:explain analyze

# Show command examples
/sc:explain implement --examples
```

### Documentation
- Main documentation: `/Docs/README.md`
- Command reference: `/Docs/reference/commands/`
- Best practices: `/Docs/guides/best-practices.md`

### Community Support
- GitHub Issues: [Report bugs](https://github.com/SuperClaude-Org/SuperClaude_Framework/issues)
- Discussions: [Ask questions](https://github.com/SuperClaude-Org/SuperClaude_Framework/discussions)

### Diagnostic Tools
```bash
# Full system diagnostic
python3 -m SuperClaude diagnose

# Check specific component
python3 -m SuperClaude check personas
python3 -m SuperClaude check mcp
python3 -m SuperClaude check commands
```

## Prevention Tips

### Best Practices to Avoid Issues

1. **Start Simple**
   - Let auto-activation work
   - Add complexity gradually
   - Trust the framework

2. **Use Absolute Paths**
   - Avoid path resolution issues
   - Ensure file access

3. **Monitor Resources**
   - Check token usage
   - Watch system resources
   - Use --safe-mode when needed

4. **Regular Updates**
   ```bash
   python3 -m SuperClaude update
   ```

5. **Test in Safe Environment**
   - Use --dry-run for testing
   - Try on small projects first
   - Backup before major operations

Remember: Most issues can be resolved by letting SuperClaude's intelligence work naturally. Over-configuration often causes more problems than it solves!
