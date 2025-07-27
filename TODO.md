# SuperClaude Framework TODO List

## Overview
This document tracks tasks for improving and extending the SuperClaude framework, with a focus on making it easier for developers to add custom slash commands.

## Task Categories

### 🎯 High Priority - Custom Command Development

#### 1. Create Developer Guide for Adding Custom Commands
- [x] **Task**: Write comprehensive documentation on adding new slash commands
- **Description**: Create a step-by-step guide for developers to extend Claude commands functionality (for users)
- **Location**: `Docs/custom-commands-guide.md`
- **Acceptance Criteria**:
  - Clear prerequisites and setup instructions
  - Step-by-step process with examples
  - Troubleshooting section
  - Best practices for command design

#### 2. Document Command Markdown Format Specification
- [x] **Task**: Define the required markdown file format for new commands
- **Description**: Document the metadata structure and required fields for command recognition
- **Location**: `Docs/command-format-specification.md`
- **Acceptance Criteria**:
  - Complete YAML frontmatter specification
  - Required vs optional fields
  - Example templates for different command types
  - Validation rules and common errors

#### 3. Test and Validate Command Addition Theory
- [x] **Task**: Verify that new commands can be added by only creating markdown files
- **Description**: Test the hypothesis that adding `.md` files to `SuperClaude/Commands/` and reinstalling is sufficient
- **Acceptance Criteria**:
  - Document the exact steps taken
  - Confirm no code changes needed in core framework
  - Identify any limitations or edge cases
  - Create test results report

### 📚 Documentation Tasks

#### 4. Create Example Command: `/sc:summary`
- [x] **Task**: Implement a proof-of-concept `/sc:summary @folder` command
- **Description**: Create a working example that summarizes folder contents
- **Location**: `SuperClaude/Commands/summary.md`
- **Acceptance Criteria**:
  - Fully functional command that works after installation
  - Demonstrates all required metadata fields
  - Includes usage examples and error handling
  - Can be used as a template for other commands

#### 5. Update README with Custom Command Instructions
- [x] **Task**: Add custom command development section to README.md
- **Description**: Include quick-start instructions for adding new commands
- **Location**: `README.md`
- **Acceptance Criteria**:
  - New section "Adding Custom Commands"
  - Links to detailed documentation
  - Quick example of adding a simple command
  - Installation/reinstallation instructions

#### 6. Create Custom Commands Directory Documentation
- [x] **Task**: Add documentation for the custom commands directory
- **Description**: Explain the purpose and usage of `SuperClaude/Commands/custom/`
- **Location**: `SuperClaude/Commands/custom/README.md`
- **Acceptance Criteria**:
  - Explain directory purpose
  - How custom commands differ from core commands
  - Versioning and update considerations

### 🔧 Technical Improvements

#### 7. Command Discovery Mechanism Documentation
- [x] **Task**: Document how the installer discovers and registers commands
- **Description**: Explain the technical process of command registration during installation
- **Location**: `Docs/technical/command-discovery.md`
- **Acceptance Criteria**:
  - Code walkthrough of discovery process
  - File naming conventions
  - Metadata parsing details
  - Integration with Claude Code

#### 8. Create Command Development Toolkit
- [x] **Task**: Build utilities to help developers create and validate commands
- **Description**: Scripts or tools to scaffold new commands and validate their format
- **Suggestions**:
  - Command template generator
  - Metadata validator
  - Local testing framework
  - Installation preview tool

## Notes
- All documentation should follow the existing style guide
- Examples should be practical and demonstrate real use cases
- Consider backwards compatibility when designing new features
- Test all examples before documenting them


# TODO

The markdown files should be in the `SuperClaude/Commands/` directory and follow the specified format, not the `SuperClaude/Commands/custom/` directory. Modify the above tasks accordingly to ensure clarity and correctness.