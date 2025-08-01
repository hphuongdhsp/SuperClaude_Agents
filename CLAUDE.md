# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SuperClaude v3 is a framework that extends Claude Code with specialized commands, personas, and MCP server integration. The project is written in Python and provides an installation framework for enhanced AI-driven development workflows.

## Common Development Commands

### Installation and Setup
```bash
# Install from PyPI
uv add SuperClaude

# Install from source
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
uv sync

# Run the installer (any of these work)
python3 -m SuperClaude install
python3 SuperClaude install
SuperClaude install

# Other operations
SuperClaude update
SuperClaude uninstall
SuperClaude backup
```

### Testing and Development
```bash
# Run a single test (example - adjust based on test framework)
python -m pytest tests/test_installer.py::test_specific_function

# Check installation
python3 -m SuperClaude install --diagnose

# Dry run installation
python3 -m SuperClaude install --dry-run
```

## High-Level Architecture

### Core Framework Structure
The SuperClaude framework consists of several interconnected systems:

1. **Command System** (`SuperClaude/Commands/`): 17 specialized slash commands for development tasks. Commands use a prefix `/sc:` to avoid conflicts. Each command has metadata specifying allowed tools and descriptions.

2. **Persona System** (`SuperClaude/Core/PERSONAS.md`): 11 domain-specific AI personalities that auto-activate based on context. Each persona has unique priorities, MCP server preferences, and quality standards.

3. **Agent System** (`SuperClaude/Agents/`): 38 specialized AI agents organized by department:
   - Engineering (7): ai-engineer, backend-architect, devops-automator, frontend-developer, mobile-app-builder, rapid-prototyper, test-writer-fixer
   - Design (5): brand-guardian, ui-designer, ux-researcher, visual-storyteller, whimsy-injector
   - Marketing (7): app-store-optimizer, content-creator, growth-hacker, instagram-curator, reddit-community-builder, tiktok-strategist, twitter-engager
   - Product (3): feedback-synthesizer, sprint-prioritizer, trend-researcher
   - Project Management (5): experiment-tracker, project-shipper, studio-producer, prd-writer, project-task-planner
   - Studio Operations (5): analytics-reporter, finance-tracker, infrastructure-maintainer, legal-compliance-checker, support-responder
   - Testing (5): api-tester, performance-benchmarker, test-results-analyzer, tool-evaluator, workflow-optimizer
   - Financial (3): kols, reporter, trump
   - Bonus (2): studio-coach, joker

4. **MCP Server Integration** (`SuperClaude/Core/MCP.md`): Integration with external Model Context Protocol servers:
   - Context7: Library documentation and patterns
   - Sequential: Complex multi-step analysis
   - Magic: UI component generation
   - Playwright: Browser automation and testing

5. **Orchestrator** (`SuperClaude/Core/ORCHESTRATOR.md`): Intelligent routing system that analyzes requests and determines optimal tool combinations, persona activation, and execution strategies. Includes wave orchestration for complex multi-stage operations.

6. **Installation System** (`setup/`): Modular component-based installer with:
   - Component registry for dynamic discovery
   - Dependency resolution
   - Multi-profile support (quick, minimal, developer)
   - Validation and rollback capabilities

### Key Design Patterns

1. **Component-Based Architecture**: All installable parts (core, commands, mcp, hooks) are self-contained components with metadata, dependencies, and installation logic.

2. **Multi-Layer Command Processing**: Commands go through parsing → context resolution → wave eligibility → execution → validation phases.

3. **Auto-Activation System**: Personas and MCP servers activate automatically based on keywords, complexity scores, and context analysis.

4. **Token Optimization**: Framework includes compression strategies and symbol systems to reduce token usage while maintaining clarity.

### Important Implementation Details

- The framework installs to `~/.claude/` by default
- Commands are prefixed with `/sc:` (e.g., `/sc:implement`, `/sc:build`)
- The installer validates that installation paths are within the user's home directory for security
- All file operations use absolute paths to prevent path traversal attacks
- The framework maintains comprehensive error handling and logging throughout

## Key Files to Understand

1. `SuperClaude/__main__.py`: Entry point for the CLI, handles command routing
2. `setup/operations/install.py`: Core installation logic and validation
3. `SuperClaude/Core/CLAUDE.md`: Entry point that references all framework documentation
4. `setup/base/installer.py`: Base installer class with component management
5. `setup/core/registry.py`: Component discovery and management system

## Recently Added Agents

### Financial Analysis Agents
- **kols**: Monitors and analyzes insights from global financial thought leaders on X (Twitter). Tracks KOLs like Ray Dalio, Lyn Alden, and others to extract actionable intelligence on macro trends, monetary policy shifts, and capital flow patterns. Particularly useful for contextualizing global trends for specific markets like Vietnam.

- **reporter**: Generates comprehensive equity research reports for Vietnamese listed companies (HOSE, HNX, UPCOM). Produces detailed company research reports analyzing fundamentals, valuation, and investment thesis, saved to `/reports/{TICKER}_research_{YYYYMMDD}.md`. Includes financial performance analysis, valuation comparisons, and investment recommendations.

- **trump**: Monitors and analyzes Donald Trump's policy announcements, executive orders, tariffs, and bills that could impact global markets and Vietnam. Tracks X (Twitter), news sources, and key opinion leaders to provide real-time analysis of Trump administration policies and their implications for trade, FDI flows, and currency markets.

### Project Management Agents
- **prd-writer**: Creates comprehensive Product Requirements Documents (PRDs) for software projects. Generates structured documentation including business goals, user personas, functional requirements, user experience flows, success metrics, technical considerations, and user stories following best practices for product management.

- **project-task-planner**: Analyzes PRDs and generates detailed, structured task lists covering all aspects of software development from initial setup through deployment and maintenance. Creates comprehensive development plans with tasks organized by phase (setup, backend, frontend, integration, testing, documentation, deployment, maintenance).

## Development Guidelines

When modifying the SuperClaude framework:
- Follow the existing component structure for new features
- Ensure all paths use absolute references
- Maintain backward compatibility with existing installations
- Add appropriate validation for user inputs
- Update relevant documentation files in the Core/ directory
- Test installation flows with both --dry-run and actual installations
