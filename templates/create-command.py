#!/usr/bin/env python3
"""
SuperClaude Command Template Generator

A simple tool to help developers create new custom commands with proper formatting.
"""

import os
import re
import sys
from pathlib import Path

# Template placeholders and their descriptions
PLACEHOLDERS = {
    'COMMAND_NAME': 'Command name (lowercase, hyphens for spaces)',
    'TITLE': 'Brief command title',
    'DESCRIPTION': 'One-line description (max 100 chars)',
    'CATEGORY': 'Category (development/analysis/documentation/testing/deployment/utility)',
    'COMPLEXITY': 'Complexity (simple/moderate/complex)',
    'TOOLS': 'Comma-separated list of tools (e.g., Read,Write,Grep)',
    'PURPOSE': 'Detailed explanation of what the command does',
    'USAGE_ARGS': 'Usage syntax (e.g., [target] [--flag value])',
    'ARGUMENTS': 'Detailed argument descriptions',
    'EXECUTION_STEPS': 'Step-by-step execution flow',
    'INTEGRATION_NOTES': 'How it integrates with Claude Code',
    'EXAMPLES': 'Practical usage examples',
    'PERFORMANCE_NOTES': 'Performance considerations',
    'ERROR_HANDLING': 'Common errors and solutions'
}

# Available tools
AVAILABLE_TOOLS = [
    'Read', 'Write', 'Edit', 'MultiEdit', 'Bash',
    'Grep', 'Glob', 'LS', 'TodoWrite', 'Task',
    'WebSearch', 'WebFetch', 'NotebookRead', 'NotebookEdit',
    'ExitPlanMode'
]

# Categories
CATEGORIES = [
    'development', 'analysis', 'documentation',
    'testing', 'deployment', 'utility'
]

# Complexity levels
COMPLEXITY_LEVELS = ['simple', 'moderate', 'complex']


def validate_command_name(name):
    """Validate command name format."""
    if not re.match(r'^[a-z][a-z0-9-]*$', name):
        return False, "Command name must be lowercase with hyphens only"
    if len(name) > 30:
        return False, "Command name too long (max 30 characters)"
    return True, ""


def validate_tools(tools_str):
    """Validate tool list."""
    tools = [t.strip() for t in tools_str.split(',')]
    invalid = [t for t in tools if t not in AVAILABLE_TOOLS]
    if invalid:
        return False, f"Invalid tools: {', '.join(invalid)}"
    return True, tools


def prompt_user(prompt, default=None, validator=None):
    """Prompt user for input with optional validation."""
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "
    
    while True:
        value = input(prompt).strip()
        if not value and default:
            value = default
        
        if validator:
            valid, result = validator(value)
            if not valid:
                print(f"Error: {result}")
                continue
            return result if isinstance(result, list) else value
        
        return value


def prompt_multiline(prompt):
    """Prompt for multiline input."""
    print(f"{prompt} (Enter empty line to finish):")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    return '\n'.join(lines)


def create_command():
    """Interactive command creation."""
    print("SuperClaude Command Template Generator")
    print("=" * 40)
    print()
    
    # Collect information
    data = {}
    
    # Command name
    data['COMMAND_NAME'] = prompt_user(
        "Command name (e.g., 'analyze-deps')",
        validator=validate_command_name
    )
    
    # Title
    data['TITLE'] = prompt_user(
        "Brief title (e.g., 'Dependency Analyzer')"
    )
    
    # Description
    while True:
        desc = prompt_user(
            "One-line description (max 100 chars)"
        )
        if len(desc) <= 100:
            data['DESCRIPTION'] = desc
            break
        print(f"Too long ({len(desc)} chars). Please shorten.")
    
    # Category
    print(f"\nCategories: {', '.join(CATEGORIES)}")
    data['CATEGORY'] = prompt_user(
        "Category",
        default="utility"
    )
    
    # Complexity
    print(f"\nComplexity: {', '.join(COMPLEXITY_LEVELS)}")
    data['COMPLEXITY'] = prompt_user(
        "Complexity",
        default="moderate"
    )
    
    # Tools
    print(f"\nAvailable tools: {', '.join(AVAILABLE_TOOLS)}")
    tools = prompt_user(
        "Required tools (comma-separated)",
        default="Read,Grep,Glob",
        validator=validate_tools
    )
    data['TOOLS'] = ','.join(tools)
    
    # Purpose
    print()
    data['PURPOSE'] = prompt_multiline("Command purpose")
    
    # Usage arguments
    data['USAGE_ARGS'] = prompt_user(
        "Usage arguments",
        default="[target] [--options]"
    )
    
    # Arguments
    print()
    data['ARGUMENTS'] = prompt_multiline("Argument descriptions")
    if not data['ARGUMENTS']:
        data['ARGUMENTS'] = "- `target` - Target for analysis"
    
    # Execution steps
    print()
    data['EXECUTION_STEPS'] = prompt_multiline("Execution steps")
    if not data['EXECUTION_STEPS']:
        data['EXECUTION_STEPS'] = "1. Validate inputs\n2. Process target\n3. Generate output"
    
    # Integration notes
    print()
    data['INTEGRATION_NOTES'] = prompt_multiline("Claude Code integration notes")
    if not data['INTEGRATION_NOTES']:
        data['INTEGRATION_NOTES'] = f"- Uses {', '.join(tools[:3])} for primary operations"
    
    # Examples
    print()
    data['EXAMPLES'] = prompt_multiline("Usage examples")
    if not data['EXAMPLES']:
        data['EXAMPLES'] = f"/sc:{data['COMMAND_NAME']} @src\n/sc:{data['COMMAND_NAME']} @. --verbose"
    
    # Performance notes
    data['PERFORMANCE_NOTES'] = prompt_user(
        "Performance notes (optional)",
        default="Optimized for standard codebases"
    )
    
    # Error handling
    data['ERROR_HANDLING'] = prompt_user(
        "Error handling notes (optional)",
        default="Validates inputs and provides clear error messages"
    )
    
    return data


def generate_command_file(data, output_dir):
    """Generate command file from template."""
    # Read template
    template_path = Path(__file__).parent / 'command-template.md'
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Replace placeholders
    content = template
    for key, value in data.items():
        content = content.replace(f'{{{key}}}', value)
    
    # Generate filename
    filename = f"{data['COMMAND_NAME']}.md"
    filepath = Path(output_dir) / filename
    
    # Write file
    with open(filepath, 'w') as f:
        f.write(content)
    
    return filepath


def main():
    """Main entry point."""
    print()
    
    # Get output directory
    default_dir = "SuperClaude/Commands"
    output_dir = prompt_user(
        "Output directory",
        default=default_dir
    )
    
    # Ensure directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Create command
    try:
        data = create_command()
        filepath = generate_command_file(data, output_dir)
        
        print()
        print("✅ Command created successfully!")
        print(f"📄 File: {filepath}")
        print()
        print("Next steps:")
        print("1. Review and edit the generated file")
        print("2. Add more detailed documentation")
        print("3. Test your command thoroughly")
        print("4. Run 'SuperClaude install' to register")
        print()
        
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()