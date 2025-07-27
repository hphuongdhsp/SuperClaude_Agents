# Command Discovery Technical Documentation

This document provides a technical deep dive into how SuperClaude discovers, parses, and registers custom commands during the installation process.

## Table of Contents
1. [Discovery Process Overview](#discovery-process-overview)
2. [File System Scanning](#file-system-scanning)
3. [Metadata Parsing](#metadata-parsing)
4. [Command Registration](#command-registration)
5. [Integration with Claude Code](#integration-with-claude-code)
6. [Implementation Details](#implementation-details)
7. [Error Handling](#error-handling)
8. [Performance Considerations](#performance-considerations)

## Discovery Process Overview

The command discovery process follows these stages:

```
1. File Discovery (scan directories)
   ↓
2. Validation (check file format)
   ↓
3. Metadata Extraction (parse YAML)
   ↓
4. Command Registration (update registry)
   ↓
5. Claude Integration (update CLAUDE.md)
```

## File System Scanning

### Directory Structure
```python
COMMANDS_DIR = "SuperClaude/Commands/"
SCAN_PATTERNS = [
    "*.md",           # Direct commands
    "*/*.md",         # Subdirectory commands
]
```

### Scanning Algorithm
```python
def discover_commands(base_path):
    """Recursively discover all command files."""
    commands = []
    
    # Walk through directory tree
    for root, dirs, files in os.walk(base_path):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, base_path)
                commands.append({
                    'path': full_path,
                    'relative': relative_path,
                    'name': extract_command_name(file)
                })
    
    return commands
```

### File Naming Convention
- **Pattern**: `command-name.md`
- **Command**: `/sc:command-name`
- **Example**: `analyze.md` → `/sc:analyze`

## Metadata Parsing

### YAML Frontmatter Extraction
```python
def parse_command_metadata(file_path):
    """Extract YAML frontmatter from command file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for YAML frontmatter
    if not content.startswith('---'):
        raise ValueError(f"No frontmatter found in {file_path}")
    
    # Extract YAML section
    yaml_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        raise ValueError(f"Invalid frontmatter in {file_path}")
    
    # Parse YAML
    yaml_content = yaml_match.group(1)
    metadata = yaml.safe_load(yaml_content)
    
    # Validate required fields
    validate_metadata(metadata, file_path)
    
    return metadata
```

### Metadata Validation
```python
REQUIRED_FIELDS = ['allowed-tools', 'description']
VALID_TOOLS = [
    'Read', 'Write', 'Edit', 'MultiEdit', 'Bash',
    'Grep', 'Glob', 'LS', 'TodoWrite', 'Task',
    'WebSearch', 'WebFetch', 'NotebookRead', 'NotebookEdit'
]

def validate_metadata(metadata, file_path):
    """Validate command metadata."""
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            raise ValueError(
                f"Missing required field '{field}' in {file_path}"
            )
    
    # Validate tools
    tools = metadata.get('allowed-tools', [])
    if not isinstance(tools, list):
        raise ValueError(
            f"'allowed-tools' must be a list in {file_path}"
        )
    
    for tool in tools:
        if tool not in VALID_TOOLS:
            raise ValueError(
                f"Invalid tool '{tool}' in {file_path}"
            )
    
    # Validate description
    desc = metadata.get('description', '')
    if not desc or len(desc) > 100:
        raise ValueError(
            f"Description must be 1-100 characters in {file_path}"
        )
```

## Command Registration

### Registry Structure
```python
class CommandRegistry:
    """Central registry for all discovered commands."""
    
    def __init__(self):
        self.commands = {}
        self.categories = defaultdict(list)
        self.tool_usage = defaultdict(list)
    
    def register(self, name, metadata, path):
        """Register a command in the registry."""
        command_data = {
            'name': name,
            'description': metadata['description'],
            'allowed_tools': metadata['allowed-tools'],
            'category': metadata.get('category', 'utility'),
            'complexity': metadata.get('complexity', 'moderate'),
            'file_path': path,
            'metadata': metadata
        }
        
        self.commands[name] = command_data
        self.categories[command_data['category']].append(name)
        
        for tool in command_data['allowed_tools']:
            self.tool_usage[tool].append(name)
```

### Registration Process
```python
def register_commands(discovered_commands):
    """Register all discovered commands."""
    registry = CommandRegistry()
    errors = []
    
    for cmd in discovered_commands:
        try:
            # Parse metadata
            metadata = parse_command_metadata(cmd['path'])
            
            # Register command
            registry.register(
                cmd['name'],
                metadata,
                cmd['path']
            )
            
            logger.info(f"Registered: /sc:{cmd['name']}")
            
        except Exception as e:
            errors.append({
                'file': cmd['path'],
                'error': str(e)
            })
            logger.error(f"Failed to register {cmd['path']}: {e}")
    
    return registry, errors
```

## Integration with Claude Code

### COMMANDS.md Generation
```python
def generate_commands_md(registry):
    """Generate COMMANDS.md content from registry."""
    content = ["# COMMANDS.md - SuperClaude Command Reference\n"]
    
    # Group by category
    for category, commands in registry.categories.items():
        content.append(f"\n## {category.title()} Commands\n")
        
        for cmd_name in sorted(commands):
            cmd = registry.commands[cmd_name]
            content.append(
                f"**`/sc:{cmd_name}`** - {cmd['description']}\n"
            )
            content.append(
                f"- Tools: {', '.join(cmd['allowed_tools'])}\n"
            )
    
    return '\n'.join(content)
```

### CLAUDE.md Update
```python
def update_claude_md(registry):
    """Update CLAUDE.md with command references."""
    claude_md_path = "~/.claude/CLAUDE.md"
    
    # Read existing content
    with open(claude_md_path, 'r') as f:
        content = f.read()
    
    # Update command count
    cmd_count = len(registry.commands)
    content = re.sub(
        r'\d+ specialized commands',
        f'{cmd_count} specialized commands',
        content
    )
    
    # Write updated content
    with open(claude_md_path, 'w') as f:
        f.write(content)
```

## Implementation Details

### Component Architecture
```
setup/
├── components/
│   └── commands.py      # Command component
├── core/
│   ├── registry.py      # Command registry
│   └── discovery.py     # Discovery logic
└── operations/
    └── install.py       # Installation orchestration
```

### Command Component
```python
class CommandsComponent(Component):
    """Component for installing command definitions."""
    
    name = "commands"
    description = "Command definitions and discovery"
    
    def install(self, context):
        """Install command files and update registry."""
        # Copy command files
        self._copy_command_files(context)
        
        # Discover all commands
        commands = discover_commands(context.target_path)
        
        # Register commands
        registry, errors = register_commands(commands)
        
        # Update framework files
        self._update_framework_files(registry, context)
        
        return {
            'installed': len(registry.commands),
            'errors': errors
        }
```

### Discovery Optimizations
```python
# Cache parsed metadata
@lru_cache(maxsize=128)
def cached_parse_metadata(file_path, mtime):
    """Cache metadata parsing results."""
    return parse_command_metadata(file_path)

# Parallel processing for large directories
def parallel_discover(base_path, num_workers=4):
    """Discover commands using parallel processing."""
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file.endswith('.md'):
                    future = executor.submit(
                        process_command_file,
                        os.path.join(root, file)
                    )
                    futures.append(future)
        
        results = []
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                logger.error(f"Discovery error: {e}")
        
        return results
```

## Error Handling

### Graceful Degradation
```python
def safe_command_discovery(base_path):
    """Discover commands with error recovery."""
    discovered = []
    errors = []
    
    try:
        # Primary discovery
        discovered = discover_commands(base_path)
    except PermissionError:
        # Fallback to readable directories only
        discovered = discover_readable_commands(base_path)
    except Exception as e:
        logger.error(f"Discovery failed: {e}")
        # Continue with empty command set
    
    return discovered, errors
```

### Validation Errors
```python
class CommandValidationError(Exception):
    """Raised when command validation fails."""
    
    def __init__(self, file_path, reason):
        self.file_path = file_path
        self.reason = reason
        super().__init__(
            f"Command validation failed for {file_path}: {reason}"
        )
```

### Error Reporting
```python
def report_discovery_errors(errors):
    """Generate user-friendly error report."""
    if not errors:
        return
    
    print("\n⚠️  Command Discovery Issues:")
    for error in errors:
        print(f"  - {error['file']}: {error['error']}")
    
    print("\nThese commands were skipped. Fix the issues and reinstall.")
```

## Performance Considerations

### Optimization Strategies

1. **Lazy Loading**
   ```python
   class LazyCommandLoader:
       """Load command metadata only when needed."""
       
       def __init__(self, file_path):
           self.file_path = file_path
           self._metadata = None
       
       @property
       def metadata(self):
           if self._metadata is None:
               self._metadata = parse_command_metadata(self.file_path)
           return self._metadata
   ```

2. **Incremental Updates**
   ```python
   def incremental_discovery(base_path, last_scan_time):
       """Discover only modified commands."""
       modified_commands = []
       
       for root, dirs, files in os.walk(base_path):
           for file in files:
               if file.endswith('.md'):
                   full_path = os.path.join(root, file)
                   mtime = os.path.getmtime(full_path)
                   
                   if mtime > last_scan_time:
                       modified_commands.append(full_path)
       
       return modified_commands
   ```

3. **Metadata Caching**
   ```python
   CACHE_FILE = "~/.claude/.command_cache.json"
   
   def load_cached_metadata():
       """Load cached command metadata."""
       if os.path.exists(CACHE_FILE):
           with open(CACHE_FILE, 'r') as f:
               return json.load(f)
       return {}
   
   def save_metadata_cache(metadata):
       """Save command metadata to cache."""
       with open(CACHE_FILE, 'w') as f:
           json.dump(metadata, f, indent=2)
   ```

### Performance Metrics

- **Discovery Time**: <100ms for 100 commands
- **Parsing Time**: <10ms per command file
- **Registration Time**: <1ms per command
- **Total Installation**: <2s for typical setup

## Future Enhancements

1. **Watch Mode**: Auto-reload commands on file changes
2. **Dependency Resolution**: Handle command dependencies
3. **Version Management**: Support command versioning
4. **Remote Commands**: Load commands from URLs
5. **Command Validation Tool**: Pre-installation validation
6. **Performance Profiling**: Built-in profiling support

## Debugging

### Debug Mode
```bash
# Enable debug logging
SUPERCLAUDE_DEBUG=1 python3 -m SuperClaude install

# Verbose discovery
python3 -m SuperClaude install --verbose

# Dry run to see what would be discovered
python3 -m SuperClaude install --dry-run
```

### Common Issues

1. **Commands Not Found**
   - Check file extension is `.md`
   - Verify file is in correct directory
   - Ensure valid YAML frontmatter

2. **Parsing Errors**
   - Validate YAML syntax
   - Check for special characters
   - Ensure proper indentation

3. **Registration Failures**
   - Verify required fields present
   - Check tool names are valid
   - Ensure unique command names

For more information, see:
- [Custom Commands Developer Guide](../custom-commands-guide.md)
- [Command Format Specification](../command-format-specification.md)