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

SuperClaude includes a comprehensive collection of specialized agents organized by department for efficient discovery and use:

### Engineering Department (`engineering/`)
- **ai-engineer**: AI/ML implementation specialist - Integrates machine learning features that actually ship
- **backend-architect**: Server architecture and API design expert - Designs scalable backend systems
- **devops-automator**: CI/CD and deployment specialist - Automates deployment without breaking things
- **frontend-developer**: UI/UX development expert - Builds blazing-fast user interfaces
- **mobile-app-builder**: Mobile app development specialist - Creates native iOS/Android experiences
- **rapid-prototyper**: MVP development specialist - Builds prototypes in days, not weeks
- **test-writer-fixer**: Testing strategy specialist - Writes tests that catch real bugs

### Design Department (`design/`)
- **brand-guardian**: Visual identity specialist - Keeps brand consistent everywhere
- **ui-designer**: Interface design expert - Designs interfaces developers can actually build
- **ux-researcher**: User experience specialist - Turns user insights into product improvements
- **visual-storyteller**: Visual communication expert - Creates visuals that convert and share
- **whimsy-injector**: Delight specialist - Adds joy to every user interaction

### Marketing Department (`marketing/`)
- **app-store-optimizer**: ASO specialist - Dominates app store search results
- **content-creator**: Multi-platform content specialist - Generates content across all platforms
- **growth-hacker**: Viral growth specialist - Finds and exploits viral growth loops
- **instagram-curator**: Visual content specialist - Masters the visual content game
- **reddit-community-builder**: Reddit engagement specialist - Wins Reddit without being banned
- **tiktok-strategist**: TikTok marketing specialist - Creates shareable marketing moments
- **twitter-engager**: Twitter engagement specialist - Rides trends to viral engagement

### Product Department (`product/`)
- **feedback-synthesizer**: User feedback specialist - Transforms complaints into features
- **sprint-prioritizer**: Sprint planning specialist - Ships maximum value in 6 days
- **trend-researcher**: Market opportunity specialist - Identifies viral opportunities

### Project Management (`project-management/`)
- **experiment-tracker**: A/B testing specialist - Provides data-driven feature validation
- **project-shipper**: Launch coordination specialist - Launches products that don't crash
- **studio-producer**: Team coordination specialist - Keeps teams shipping, not meeting

### Studio Operations (`studio-operations/`)
- **analytics-reporter**: Data analysis specialist - Turns data into actionable insights
- **finance-tracker**: Financial management specialist - Keeps the studio profitable
- **infrastructure-maintainer**: Infrastructure specialist - Scales without breaking the bank
- **legal-compliance-checker**: Compliance specialist - Stays legal while moving fast
- **support-responder**: Customer support specialist - Turns angry users into advocates

### Testing & Benchmarking (`testing/`)
- **api-tester**: API testing specialist - Ensures APIs work under pressure
- **performance-benchmarker**: Performance optimization specialist - Makes everything faster
- **test-results-analyzer**: Test analysis specialist - Finds patterns in test failures
- **tool-evaluator**: Tool assessment specialist - Chooses tools that actually help
- **workflow-optimizer**: Process optimization specialist - Eliminates workflow bottlenecks

### Bonus Agents
- **studio-coach**: AI coordination specialist - Rallies the AI troops to excellence
- **joker**: Morale specialist - Lightens the mood with tech humor

## Using Agents

Agents are designed to work seamlessly with Claude Code. Each agent has:

1. **Specialized Knowledge**: Domain-specific expertise and best practices
2. **Tool Preferences**: Optimized tool selection for their domain
3. **Unique Approach**: Tailored problem-solving methodology
4. **Quality Standards**: Domain-appropriate validation and checks

### Directory Structure

Agents are organized by department for easy discovery:

```
SuperClaude/Agents/
├── engineering/
│   ├── ai-engineer.md
│   ├── backend-architect.md
│   ├── devops-automator.md
│   ├── frontend-developer.md
│   ├── mobile-app-builder.md
│   ├── rapid-prototyper.md
│   └── test-writer-fixer.md
├── design/
│   ├── brand-guardian.md
│   ├── ui-designer.md
│   ├── ux-researcher.md
│   ├── visual-storyteller.md
│   └── whimsy-injector.md
├── marketing/
│   ├── app-store-optimizer.md
│   ├── content-creator.md
│   ├── growth-hacker.md
│   ├── instagram-curator.md
│   ├── reddit-community-builder.md
│   ├── tiktok-strategist.md
│   └── twitter-engager.md
├── product/
│   ├── feedback-synthesizer.md
│   ├── sprint-prioritizer.md
│   └── trend-researcher.md
├── project-management/
│   ├── experiment-tracker.md
│   ├── project-shipper.md
│   └── studio-producer.md
├── studio-operations/
│   ├── analytics-reporter.md
│   ├── finance-tracker.md
│   ├── infrastructure-maintainer.md
│   ├── legal-compliance-checker.md
│   └── support-responder.md
├── testing/
│   ├── api-tester.md
│   ├── performance-benchmarker.md
│   ├── test-results-analyzer.md
│   ├── tool-evaluator.md
│   └── workflow-optimizer.md
└── bonus/
    ├── joker.md
    └── studio-coach.md
```

### Agent Structure

Each agent file contains:
- **name**: Unique identifier for the agent
- **description**: When and how to use the agent with detailed examples
- **tools**: Allowed Claude Code tools
- **color**: Visual identifier (optional)
- **prompt**: Detailed instructions and behavior patterns optimized for 6-day development cycles

### Best Practices

1. **Choose the Right Agent**: Select agents based on your specific task and department
2. **Leverage Department Organization**: Browse by department to find the most relevant specialist
3. **Provide Context**: Give agents relevant background information about your project
4. **Follow Agent Guidance**: Each agent has specific workflows optimized for their domain and 6-day sprints
5. **Combine Agents**: Use multiple agents for complex, multi-domain projects
6. **Trust Proactive Agents**: Some agents auto-activate in specific contexts (studio-coach, test-writer-fixer, whimsy-injector)
7. **Iterate Quickly**: Agents support rapid development and frequent iteration

## Agent Examples

### Engineering Tasks
```markdown
# Rapid prototyping
Agent: rapid-prototyper
Task: Create a new app that helps people overcome phone anxiety

# Backend architecture
Agent: backend-architect
Task: Design microservices architecture for e-commerce platform

# Testing
Agent: test-writer-fixer
Task: Write comprehensive tests for the payment processing module
```

### Design Tasks
```markdown
# UI design
Agent: ui-designer
Task: Create a dashboard for displaying user analytics

# Adding delight
Agent: whimsy-injector
Task: Make this loading screen more fun and engaging

# User research
Agent: ux-researcher
Task: Analyze user feedback to improve onboarding flow
```

### Marketing Tasks
```markdown
# TikTok strategy
Agent: tiktok-strategist
Task: Create viral TikTok content ideas for our meditation app

# App store optimization
Agent: app-store-optimizer
Task: Optimize our app listing to increase downloads

# Community building
Agent: reddit-community-builder
Task: Build a community around our productivity app on Reddit
```

### Product & Project Management
```markdown
# Feature prioritization
Agent: sprint-prioritizer
Task: Prioritize features for our 6-day sprint to maximize user value

# Trend research
Agent: trend-researcher
Task: What's trending on TikTok that we could build an app around?

# Launch coordination
Agent: project-shipper
Task: Coordinate the launch of our new collaboration feature
```

## Creating Custom Agents

While SuperClaude comes with comprehensive pre-built agents, you can create custom agents:

1. Create a new `.md` file in the appropriate department folder in `~/.claude/agents/`
2. Add required frontmatter (name, description with examples)
3. Define the agent's behavior and approach for 6-day development cycles
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
- Enhanced agent collaboration patterns
- Department-specific agent workflows
- Agent performance metrics and analytics
- Community agent contributions
- Agent versioning and updates
- Cross-department coordination features

## Support

For issues or suggestions regarding agents:
- Report issues at: https://github.com/hphuongdhsp/SuperClaude_Agents/issues
- Browse existing agents by department for examples
- Consult the SuperClaude documentation
- Check the comprehensive agent descriptions in the `README agents.md` file
