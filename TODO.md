Debug installation issues with SuperClaude_Agents [RESOLVED]

Issue: The installation of SuperClaude_Agents failed with YAML parsing errors for certain agent files and metadata registration issues.

## Problems Identified

1. **YAML Parsing Failure**: Agent files with complex multi-line descriptions containing embedded YAML examples (code-refactorer.md, content-writer.md, etc.) caused the YAML parser to fail.

2. **Metadata Registration**: The agents component wasn't being registered in metadata because `_post_install()` wasn't being called after installation.

## Solutions Implemented

### 1. Enhanced YAML Parsing (agents.py)
- Added robust error handling for YAML parsing failures
- Implemented fallback regex-based parsing for complex frontmatter
- Special handling for multi-line descriptions with embedded code examples
- Improved parsing for fields like `tools:`, `color:`, and `examples:`

### 2. Fixed Installation Flow (agents.py)
- Modified `_install()` method to call `_post_install()` after successful installation
- This ensures metadata registration happens correctly
- Component is now properly registered in the system metadata

### 3. Improved Validation Methods
- Updated `_validate_agent_file()` to handle complex YAML structures
- Enhanced `_get_installed_agent_names()` with better error handling
- Improved `_display_agent_summary()` to handle multi-line descriptions gracefully

## Impact

These minimal changes ensure:
- All agent files can be parsed regardless of description complexity
- Agents component is properly registered in system metadata
- Installation validation passes successfully
- Better error handling and fallback mechanisms

The fixes maintain backward compatibility while resolving the installation issues.