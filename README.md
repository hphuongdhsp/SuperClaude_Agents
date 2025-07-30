# SuperClaude v3 🚀 (Forked)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0--fork-blue.svg)](https://github.com/hphuongdhsp/SuperClaude_Agents)
[![GitHub issues](https://img.shields.io/github/issues/hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/graphs/contributors)

A framework that extends Claude Code with specialized commands, personas, and MCP server integration.

**🌏 Languages**: [English](README.md) | [Tiếng Việt](README_vi.md)

**📢 Status**: This is a fork of the original SuperClaude v3 project. This fork aims to continue development and provide installation from source.

## What is SuperClaude? 🤔

SuperClaude tries to make Claude Code more helpful for development work by adding:
- 🛠️ **17 specialized commands** for common dev tasks (some work better than others!)
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
- 17 slash commands for various development tasks
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
We focused on 17 essential commands for the most common tasks:

**Development**: `/sc:implement`, `/sc:build`, `/sc:design`
**Analysis**: `/sc:analyze`, `/sc:troubleshoot`, `/sc:explain`
**Quality**: `/sc:improve`, `/sc:test`, `/sc:cleanup`
**Others**: `/sc:document`, `/sc:git`, `/sc:estimate`, `/sc:task`, `/sc:todo`, `/sc:index`, `/sc:load`, `/sc:spawn`

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

Choose your operating system below for detailed step-by-step instructions:

## 🍎 Installation for Mac Users

### Prerequisites
First, let's make sure you have everything you need:

**Step 1: Install Homebrew (if you don't have it)**
1. Open Terminal (press `Cmd + Space`, type "Terminal", and press Enter)
2. Copy and paste this command:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Press Enter and follow the prompts
4. When finished, restart Terminal

**Step 2: Install Python 3**
1. In Terminal, run:
   ```bash
   brew install python3
   ```
2. Verify Python is installed:
   ```bash
   python3 --version
   ```
   You should see something like "Python 3.11.x" or higher

**Step 3: Install Git (if you don't have it)**
```bash
brew install git
```

### Installation Process

**Step 4: Download SuperClaude**
1. In Terminal, navigate to where you want to install SuperClaude (e.g., your home folder):
   ```bash
   cd ~
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
   ```
3. Enter the SuperClaude directory:
   ```bash
   cd SuperClaude_Agents
   ```

**Step 5: Install UV (recommended package manager)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then restart your terminal or run:
```bash
source ~/.bashrc
```

**Step 6: Install SuperClaude**
```bash
uv sync
```

**Step 7: Run the SuperClaude installer**
```bash
python3 -m SuperClaude install
```

**That's it! 🎉** SuperClaude is now installed and ready to use with Claude Code.

---

## 🐧 Installation for Ubuntu Users

### Prerequisites
First, let's make sure your system is up to date and has everything needed:

**Step 1: Update your system**
1. Open Terminal (press `Ctrl + Alt + T`)
2. Update package lists:
   ```bash
   sudo apt update
   ```
3. Upgrade installed packages:
   ```bash
   sudo apt upgrade -y
   ```

**Step 2: Install Python 3 and pip**
```bash
sudo apt install python3 python3-pip python3-venv git curl -y
```

**Step 3: Verify Python installation**
```bash
python3 --version
```
You should see something like "Python 3.8.x" or higher

### Installation Process

**Step 4: Download SuperClaude**
1. Navigate to your home directory:
   ```bash
   cd ~
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
   ```
3. Enter the SuperClaude directory:
   ```bash
   cd SuperClaude_Agents
   ```

**Step 5: Install UV (recommended package manager)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then reload your shell configuration:
```bash
source ~/.bashrc
```
Or restart your terminal.

**Step 6: Install SuperClaude**
```bash
uv sync
```

**Step 7: Run the SuperClaude installer**
```bash
python3 -m SuperClaude install
```

**That's it! 🎉** SuperClaude is now installed and ready to use with Claude Code.

---

## 🔄 Alternative Installation Methods

### Using UV (Advanced Users)
If you prefer using `uv` directly for better performance:

```bash
# After cloning the repository:
cd SuperClaude_Agents
uv venv
source .venv/bin/activate  # On Mac/Linux
uv sync
```

### Using UVX (Cross-platform)
```bash
git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
cd SuperClaude_Agents
uvx run uv sync
```

---

## 📋 Installation Verification

After installation, verify everything works:

1. **Check if SuperClaude is installed:**
   ```bash
   python3 -m SuperClaude --help
   ```

2. **Test a basic command:**
   ```bash
   SuperClaude install --help
   ```

If you see help information, congratulations! SuperClaude is properly installed.

---

## 🚨 Troubleshooting Common Issues

**Problem: "command not found: python3"**
- **Mac**: Install Python with `brew install python3`
- **Ubuntu**: Install with `sudo apt install python3`

**Problem: "command not found: git"**
- **Mac**: Install with `brew install git`
- **Ubuntu**: Install with `sudo apt install git`

**Problem: "Permission denied" errors**
- Never use `sudo` with SuperClaude installation
- Make sure you're installing in your home directory

**Problem: "uv: command not found"**
- The uv installer script may need you to restart your terminal
- Or manually source your shell config: `source ~/.bashrc`

**Need more help?** Open an issue on our [GitHub page](https://github.com/hphuongdhsp/SuperClaude_Agents/issues).

## ⚙️ Installer Options

After following the platform-specific installation steps above, you can customize your SuperClaude installation with these options:

### Installation Profiles

**Quick Setup (Recommended for most users)**
```bash
python3 -m SuperClaude install
```

**Interactive Selection (Choose components)**
```bash
python3 -m SuperClaude install --interactive
```

**Minimal Installation (Just core framework)**
```bash
python3 -m SuperClaude install --minimal
```

**Developer Setup (Everything included)**
```bash
python3 -m SuperClaude install --profile developer
```

### Alternative Command Formats

You can also use these equivalent formats:

**Python Module Style:**
```bash
python3 -m SuperClaude install [options]
```

**Direct Python Execution:**
```bash
python3 SuperClaude install [options]
```

**Simple Bash Command (if available in PATH):**
```bash
SuperClaude install [options]
```

### Get Help
```bash
python3 -m SuperClaude install --help
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

## Adding Custom Commands 🛠️

### Quick Start
You can extend SuperClaude with your own custom slash commands! Here's how:

1. **Create a markdown file** in `SuperClaude/Commands/custom/`
2. **Add required metadata** (YAML frontmatter)
3. **Run** `SuperClaude install` to register

Example custom command:
```markdown
---
allowed-tools: [Read, Grep, Glob]
description: "Analyze and summarize folder contents"
---

# /sc:mysummary - Custom Folder Analyzer

## Purpose
Provide insights into folder structure and contents.

## Usage
```
/sc:mysummary @folder
```
```

That's it! Your command is now available in Claude Code.

📚 **For detailed instructions**, see:
- [Custom Commands Developer Guide](Docs/custom-commands-guide.md)
- [Command Format Specification](Docs/command-format-specification.md)

## Using /sc:todo Efficiently 📝

The `/sc:todo` command helps reformat your TODO.md file to make it more understandable for Claude Code. Here's how to use it effectively:

### When to Use /sc:todo
- When your TODO.md has unclear or poorly formatted tasks
- Before starting work to organize your task list
- After brainstorming to structure your ideas
- When Claude Code struggles to understand your tasks

### Basic Usage
```bash
# Reformat with default settings
/sc:todo

# Create high-level strategic tasks
/sc:todo --high

# Break down into detailed action items
/sc:todo --low

# Apply structured formatting with clear categories
/sc:todo --structured --actionable
```

### Example Workflow
1. **Write your tasks** in TODO.md (don't worry about formatting)
2. **Run** `/sc:todo --structured --actionable` to reformat
3. **Review** the reformatted tasks
4. **Use** other commands like `/sc:implement` or `/sc:improve` to work on tasks

### Tips for Better Results
- Include context in your original TODO.md (e.g., "implement user auth" → "implement JWT-based user authentication for the REST API")
- Group related tasks together
- Use `/sc:todo --commands` to get command suggestions for each task
- Combine flags for best results: `/sc:todo --low --actionable --commands`

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
