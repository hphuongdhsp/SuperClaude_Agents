# SuperClaude Agents Guide

## Overview

SuperClaude Agents are specialized AI assistant configurations that enhance Claude Code with domain-specific expertise and behaviors. Each agent has a unique personality, tools, and focus area to help with specific types of tasks.

## Installation

Agents are automatically installed when you install SuperClaude using the quick or developer profiles:

```bash
# Install with agents included
python3 -m SuperClaude install --profile quick

# Or install agents separately
python3 -m SuperClaude install --components agents
```

After installation, agents are available in `~/.claude/agents/`.

## Available Agents

SuperClaude includes 35 specialized agents:

### Development Agents
- **ai-engineer**: AI/ML implementation specialist
- **backend-architect**: Server architecture and API design expert
- **cloud-architect**: Cloud infrastructure and deployment specialist
- **frontend-developer**: UI/UX development expert
- **frontend-designer**: Visual design and user experience specialist
- **golang-pro**: Go language specialist
- **graphql-architect**: GraphQL API design expert
- **mobile-developer**: Mobile app development specialist
- **python-pro**: Python development expert

### Code Quality Agents
- **code-reviewer**: Code quality and security reviewer
- **code-refactorer**: Code improvement and restructuring specialist
- **debugger**: Bug fixing and troubleshooting expert
- **test-automator**: Testing strategy and automation specialist

### Infrastructure & Operations
- **cloud-architect**: Cloud platform specialist
- **database-optimizer**: Database performance expert
- **deployment-engineer**: CI/CD and deployment specialist
- **devops-troubleshooter**: Infrastructure problem solver
- **incident-responder**: Production issue handler

### Specialized Domains
- **data-engineer**: Data pipeline specialist
- **data-scientist**: Data analysis and modeling expert
- **ml-engineer**: Machine learning implementation specialist
- **payment-integration**: Payment systems expert
- **performance-engineer**: System optimization specialist
- **quant-analyst**: Financial modeling specialist
- **security-auditor**: Security assessment expert

### Documentation & Planning
- **api-documenter**: API documentation specialist
- **architect-review**: Architecture assessment expert
- **content-writer**: Technical writing specialist
- **prd-writer**: Product requirements specialist
- **project-plan-task**: Project planning expert
- **prompt-engineer**: AI prompt optimization specialist

### Other Specialists
- **context-manager**: Context optimization expert
- **dx-optimizer**: Developer experience improver
- **legacy-modernizer**: Legacy system upgrade specialist
- **vibe-coding-coach**: Pair programming companion

## Using Agents

Agents are designed to work seamlessly with Claude Code. Each agent has:

1. **Specialized Knowledge**: Domain-specific expertise and best practices
2. **Tool Preferences**: Optimized tool selection for their domain
3. **Unique Approach**: Tailored problem-solving methodology
4. **Quality Standards**: Domain-appropriate validation and checks

### Agent Structure

Each agent file contains:
- **name**: Unique identifier for the agent
- **description**: When and how to use the agent
- **tools**: Allowed Claude Code tools
- **color**: Visual identifier (optional)
- **prompt**: Detailed instructions and behavior patterns

### Best Practices

1. **Choose the Right Agent**: Select agents based on your specific task
2. **Provide Context**: Give agents relevant background information
3. **Follow Agent Guidance**: Each agent has specific workflows optimized for their domain
4. **Combine Agents**: Use multiple agents for complex, multi-domain projects

## Agent Examples

### Code Review Example
```markdown
# After implementing a feature, use the code-reviewer agent
Agent: code-reviewer
Task: Review the authentication implementation for security and quality
```

### Architecture Planning Example
```markdown
# For system design, use the architect agents
Agent: backend-architect
Task: Design microservices architecture for e-commerce platform
```

### Performance Optimization Example
```markdown
# For performance issues, use specialized agents
Agent: performance-engineer
Task: Optimize database queries causing slow page loads
```

## Creating Custom Agents

While SuperClaude comes with 35 pre-built agents, you can create custom agents:

1. Create a new `.md` file in `~/.claude/agents/`
2. Add required frontmatter (name, description)
3. Define the agent's behavior and approach
4. Specify allowed tools and preferences

Example custom agent structure:
```markdown
---
name: my-custom-agent
description: Specialized agent for specific domain
tools: Read, Write, Edit, MultiEdit, Grep
---

You are a specialized assistant for [domain]. Your approach...
```

## Troubleshooting

### Agent Not Loading
- Verify the agent file exists in `~/.claude/agents/`
- Check that the frontmatter is valid YAML
- Ensure required fields (name, description) are present

### Agent Behavior Issues
- Review the agent's prompt for clarity
- Verify tool permissions are appropriate
- Check for conflicts with other configurations

## Future Enhancements

The SuperClaude team is working on:
- Agent marketplace for community contributions
- Agent versioning and updates
- Agent dependency management
- Performance metrics and analytics
- Cross-agent collaboration features

## Support

For issues or suggestions regarding agents:
- Report issues at: https://github.com/SuperClaude-Org/SuperClaude_Framework/issues
- Check existing agents for examples
- Consult the SuperClaude documentation