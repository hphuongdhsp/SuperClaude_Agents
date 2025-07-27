# SuperClaude v3 🚀 (Forked)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0--fork-blue.svg)](https://github.com/hphuongdhsp/SuperClaude_Agents)
[![GitHub issues](https://img.shields.io/github/issues/hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/graphs/contributors)

A framework that extends Claude Code with specialized commands, personas, and MCP server integration.

**📢 Status**: This is a fork of the original SuperClaude v3 project. The original repository is no longer maintained. This fork aims to continue development and provide installation from source.

## What is SuperClaude? 🤔

SuperClaude tries to make Claude Code more helpful for development work by adding:
- 🛠️ **16 specialized commands** for common dev tasks (some work better than others!)
- 🤖 **35 AI agents** with specialized expertise (code review, architecture, testing, etc.)
- 🎭 **Smart personas** that usually pick the right expert for different domains 
- 🔧 **MCP server integration** for docs, UI components, and browser automation
- 📋 **Task management** that tries to keep track of progress
- ⚡ **Token optimization** to help with longer conversations

This is what we've been building to make development workflows smoother. Still rough around the edges, but getting better! 😊

## Current Status 📊

✅ **What's Working Well:**
- Installation suite (rewritten from the ground up)
- Core framework with 9 documentation files 
- 16 slash commands for various development tasks
- 35 specialized AI agents for domain-specific assistance
- MCP server integration (Context7, Sequential, Magic, Playwright)
- Unified CLI installer for easy setup

⚠️ **Known Issues:**
- This is an initial release - bugs are expected
- Some features may not work perfectly yet
- Documentation is still being improved
- Hooks system was removed (coming back in v4)

## Key Features ✨

### Commands 🛠️
We focused on 16 essential commands for the most common tasks:

**Development**: `/sc:implement`, `/sc:build`, `/sc:design`  
**Analysis**: `/sc:analyze`, `/sc:troubleshoot`, `/sc:explain`  
**Quality**: `/sc:improve`, `/sc:test`, `/sc:cleanup`  
**Others**: `/sc:document`, `/sc:git`, `/sc:estimate`, `/sc:task`, `/sc:index`, `/sc:load`, `/sc:spawn`

### Smart Personas 🎭
AI specialists that try to jump in when they seem relevant:
- 🏗️ **architect** - Systems design and architecture stuff
- 🎨 **frontend** - UI/UX and accessibility  
- ⚙️ **backend** - APIs and infrastructure
- 🔍 **analyzer** - Debugging and figuring things out
- 🛡️ **security** - Security concerns and vulnerabilities
- ✍️ **scribe** - Documentation and writing
- *...and 5 more specialists*

*(They don't always pick perfectly, but usually get it right!)*

### AI Agents 🤖
35 specialized agents for specific tasks and domains:
- **Development**: `ai-engineer`, `backend-architect`, `frontend-developer`, `golang-pro`, `python-pro`
- **Code Quality**: `code-reviewer`, `code-refactorer`, `debugger`, `test-automator`
- **Infrastructure**: `cloud-architect`, `deployment-engineer`, `devops-troubleshooter`
- **Specialized**: `data-scientist`, `ml-engineer`, `security-auditor`, `performance-engineer`
- **Documentation**: `api-documenter`, `content-writer`, `prompt-engineer`

Each agent has unique expertise, tool preferences, and approaches. See [Docs/agents-guide.md](Docs/agents-guide.md) for details.

### MCP Integration 🔧
External tools that connect when useful:
- **Context7** - Grabs official library docs and patterns 
- **Sequential** - Helps with complex multi-step thinking  
- **Magic** - Generates modern UI components 
- **Playwright** - Browser automation and testing stuff

*(These work pretty well when they connect properly! 🤞)*

## ⚠️ Upgrading from v2? Important!

If you're coming from SuperClaude v2, you'll need to clean up first:

1. **Uninstall v2** using its uninstaller if available
2. **Manual cleanup** - delete these if they exist:
   - `SuperClaude/`
   - `~/.claude/shared/`
   - `~/.claude/commands/` 
   - `~/.claude/CLAUDE.md`
4. **Then proceed** with v3 installation below

This is because v3 has a different structure and the old files can cause conflicts.

### 🔄 **Key Change for v2 Users**
**The `/build` command changed!** In v2, `/build` was used for feature implementation. In v3:
- `/sc:build` = compilation/packaging only 
- `/sc:implement` = feature implementation (NEW!)

**Migration**: Replace `v2 /build myFeature` with `v3 /sc:implement myFeature`

## Installation 📦

SuperClaude installation is a **two-step process**:
1. First install the Python package
2. Then run the installer to set up Claude Code integration

### Step 1: Install the Package

**Install from Source (This Repository)**
```bash
git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
cd SuperClaude_Agents
uv sync
```

> **Note**: PyPI installation is not available for this fork. Please install from source using the instructions above.
### 🔧 UV / UVX Setup Guide

SuperClaude v3 also supports installation via [`uv`](https://github.com/astral-sh/uv) (a faster, modern Python package manager) or `uvx` for cross-platform usage.

### 🌀 Install with `uv`

Make sure `uv` is installed:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

> Or follow instructions from: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

Once `uv` is available, you can install SuperClaude like this:

```bash
# After cloning the repository:
cd SuperClaude_Agents
uv venv
source .venv/bin/activate
uv sync
```

### ⚡ Install with `uvx` (Cross-platform CLI)

If you’re using `uvx`, just run:

```bash
# Clone and install from source:
git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
cd SuperClaude_Agents
uvx run uv sync
```

### ✅ Finish Installation

After installing, continue with the usual installer step:

```bash
python3 -m SuperClaude install
```

Or using bash-style CLI:

```bash
SuperClaude install
```

### 🧠 Note:

* `uv` provides better caching and performance.
* Compatible with Python 3.8+ and works smoothly with SuperClaude.
* This fork requires installation from source - PyPI packages are not available.

---
**Missing Python?** Install Python 3.7+ first:
```bash
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 python3-pip

# macOS  
brew install python3

# Windows
# Download from https://python.org/downloads/
```

### Step 2: Run the Installer

After installing the package, run the SuperClaude installer to configure Claude Code (You can use any of the method):
### ⚠️ Important Note 
**After installing the SuperClaude.**
**You can use `SuperClaude commands`
, `python3 -m SuperClaude commands` or also `python3 SuperClaude commands`**
```bash
# Quick setup (recommended for most users)
python3 SuperClaude install

# Interactive selection (choose components)
python3 SuperClaude install --interactive

# Minimal install (just core framework)
python3 SuperClaude install --minimal

# Developer setup (everything included)
python3 SuperClaude install --profile developer

# See all available options
python3 SuperClaude install --help
```
### Or Python Modular Usage
```bash
# Quick setup (recommended for most users)
python3 -m SuperClaude install

# Interactive selection (choose components)
python3 -m SuperClaude install --interactive

# Minimal install (just core framework)
python3 -m SuperClaude install --minimal

# Developer setup (everything included)
python3 -m SuperClaude install --profile developer

# See all available options
python3 -m SuperClaude install --help
```
### Simple bash Command Usage 
```bash
# Quick setup (recommended for most users)
SuperClaude install

# Interactive selection (choose components)
SuperClaude install --interactive

# Minimal install (just core framework)
SuperClaude install --minimal

# Developer setup (everything included)
SuperClaude install --profile developer

# See all available options
SuperClaude install --help
```

**That's it! 🎉** The installer handles everything: framework files, MCP servers, and Claude Code configuration.

## How It Works 🔄

SuperClaude tries to enhance Claude Code through:

1. **Framework Files** - Documentation installed to `~/.claude/` that guides how Claude responds
2. **Slash Commands** - 16 specialized commands for different dev tasks  
3. **MCP Servers** - External services that add extra capabilities (when they work!)
4. **Smart Routing** - Attempts to pick the right tools and experts based on what you're doing

Most of the time it plays nicely with Claude Code's existing stuff. 🤝

## What's Coming in v4 🔮

We're hoping to work on these things for the next version:
- **Hooks System** - Event-driven stuff (removed from v3, trying to redesign it properly)
- **MCP Suite** - More external tool integrations  
- **Better Performance** - Trying to make things faster and less buggy
- **More Personas** - Maybe a few more domain specialists
- **Cross-CLI Support** - Might work with other AI coding assistants

*(No promises on timeline though - we're still figuring v3 out! 😅)*

## Configuration ⚙️

After installation, you can customize SuperClaude by editing:
- `~/.claude/settings.json` - Main configuration
- `~/.claude/*.md` - Framework behavior files

Most users probably won't need to change anything - it usually works okay out of the box. 🎛️

## Documentation 📖

Want to learn more? Check out our guides:

- 📚 [**User Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/superclaude-user-guide.md) - Complete overview and getting started
- 🛠️ [**Commands Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/commands-guide.md) - All 16 slash commands explained  
- 🏳️ [**Flags Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/flags-guide.md) - Command flags and options
- 🎭 [**Personas Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/personas-guide.md) - Understanding the persona system
- 📦 [**Installation Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/installation-guide.md) - Detailed installation instructions

These guides have more details than this README and are kept up to date.

## Contributing 🤝

We welcome contributions! Areas where we could use help:
- 🐛 **Bug Reports** - Let us know what's broken
- 📝 **Documentation** - Help us explain things better  
- 🧪 **Testing** - More test coverage for different setups
- 💡 **Ideas** - Suggestions for new features or improvements

The codebase is pretty straightforward Python + documentation files.

## Project Structure 📁

```
SuperClaude/
├── setup.py               # pypi setup file
├── SuperClaude/           # Framework files  
│   ├── Core/              # Behavior documentation (COMMANDS.md, FLAGS.md, etc.)
│   ├── Commands/          # 16 slash command definitions
│   └── Settings/          # Configuration files
├── setup/                 # Installation system
└── profiles/              # Installation profiles (quick, minimal, developer)
```

## Architecture Notes 🏗️

The v3 architecture focuses on:
- **Simplicity** - Removed complexity that wasn't adding value
- **Reliability** - Better installation and fewer breaking changes  
- **Modularity** - Pick only the components you want
- **Performance** - Faster operations with smarter caching

We learned a lot from v2 and tried to address the main pain points.

## FAQ 🙋

**Q: Why was the hooks system removed?**  
A: It was getting complex and buggy. We're redesigning it properly for v4.

**Q: Does this work with other AI assistants?**  
A: Currently Claude Code only, but v4 will have broader compatibility.

**Q: Is this stable enough for daily use?**  
A: The basic stuff works pretty well, but definitely expect some rough edges since it's a fresh release. Probably fine for experimenting! 🧪

## SuperClaude Contributors

[![Contributors](https://contrib.rocks/image?repo=hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/graphs/contributors)

> **Note**: This project is a fork of the original [SuperClaude](https://github.com/NomenAK/SuperClaude) project.

## License

MIT - [See LICENSE file for details](https://opensource.org/licenses/MIT)

## Star History

<a href="https://www.star-history.com/#hphuongdhsp/SuperClaude_Agents&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=hphuongdhsp/SuperClaude_Agents&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=hphuongdhsp/SuperClaude_Agents&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=hphuongdhsp/SuperClaude_Agents&type=Date" />
 </picture>
</a>
---

*Built by developers who got tired of generic responses. Hope you find it useful! 🙂*

---
