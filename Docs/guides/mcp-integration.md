# MCP Server Integration Guide 🔌

Master the power of SuperClaude's Model Context Protocol (MCP) server integrations for enhanced AI capabilities.

## Table of Contents

1. [Overview](#overview)
2. [Context7 - Documentation & Patterns](#context7---documentation--patterns)
3. [Sequential - Complex Analysis](#sequential---complex-analysis)
4. [Magic - UI Component Generation](#magic---ui-component-generation)
5. [Playwright - Browser Automation & Testing](#playwright---browser-automation--testing)
6. [Server Coordination](#server-coordination)
7. [Performance Optimization](#performance-optimization)
8. [Troubleshooting](#troubleshooting)

## Overview

### What are MCP Servers?

MCP (Model Context Protocol) servers extend SuperClaude with specialized capabilities:
- **External Intelligence**: Access to specialized knowledge and tools
- **Domain Expertise**: Purpose-built for specific tasks
- **Auto-Activation**: Intelligent selection based on context
- **Seamless Integration**: Works transparently with commands

### Available Servers

| Server | Purpose | Auto-Activation Triggers |
|--------|---------|-------------------------|
| **Context7** | Library docs, patterns | Import statements, framework keywords |
| **Sequential** | Multi-step analysis | Complex problems, --think flags |
| **Magic** | UI components | Component keywords, frontend work |
| **Playwright** | Testing, automation | Test keywords, E2E, performance |

## Context7 - Documentation & Patterns

### 📚 Purpose
Access official library documentation, code patterns, and best practices.

### 🎯 When to Use

#### Automatic Activation
```bash
# Detects library imports
/sc:implement "React component with hooks"  # Auto-activates Context7

# Framework-specific work
/sc:build "Express API with middleware"  # Auto-activates Context7
```

#### Manual Activation
```bash
# Force Context7 for documentation
/sc:analyze library-code --c7

# Combine with implementation
/sc:implement feature --c7 --with-patterns
```

### 💡 Best Practices

#### Library Pattern Discovery
```bash
# Find the right patterns
/sc:analyze "Redux implementation" --c7
/sc:explain "React hooks best practices" --c7
```

#### Implementation with Documentation
```bash
# Get patterns while building
/sc:implement "authentication with Passport.js" --c7
/sc:build "GraphQL server with Apollo" --c7
```

### 📖 Supported Libraries

Context7 covers major libraries including:
- **Frontend**: React, Vue, Angular, Svelte
- **Backend**: Express, Django, Flask, FastAPI
- **Database**: MongoDB, PostgreSQL, Redis
- **Testing**: Jest, Mocha, Cypress
- **And many more...**

### 🔧 Advanced Usage

```bash
# Multi-library integration
/sc:implement "React + Redux + TypeScript app" --c7

# Pattern extraction
/sc:analyze "authentication patterns" --c7 --focus best-practices

# Documentation generation
/sc:document my-code --c7 --with-examples
```

## Sequential - Complex Analysis

### 🧠 Purpose
Multi-step problem solving and systematic analysis for complex scenarios.

### 🎯 When to Use

#### Automatic Activation
```bash
# Complex debugging
/sc:troubleshoot "memory leak in production" # Auto-activates Sequential

# Deep analysis
/sc:analyze system --think-hard  # Auto-activates Sequential
```

#### Manual Activation
```bash
# Force Sequential for structured thinking
/sc:analyze architecture --seq

# Combine with deep thinking
/sc:troubleshoot issue --seq --ultrathink
```

### 💡 Best Practices

#### Systematic Debugging
```bash
# Step-by-step problem solving
/sc:troubleshoot "race condition" --seq --think

# Root cause analysis
/sc:analyze bug-report --seq --focus root-cause
```

#### Architecture Analysis
```bash
# System design review
/sc:analyze system-architecture --seq --comprehensive

# Performance bottleneck identification
/sc:analyze performance --seq --with-metrics
```

### 🔍 Analysis Capabilities

Sequential excels at:
- **Problem Decomposition**: Breaking complex issues into steps
- **Hypothesis Testing**: Systematic validation of theories
- **Relationship Mapping**: Understanding system interactions
- **Decision Trees**: Structured decision-making

### 🔧 Advanced Usage

```bash
# Multi-phase analysis
/sc:analyze complex-system --seq --wave-mode

# Combine with other servers
/sc:troubleshoot full-stack-issue --seq --c7 --play

# Iterative problem solving
/sc:troubleshoot persistent-bug --seq --loop
```

## Magic - UI Component Generation

### 🎨 Purpose
Modern UI component generation with design system integration.

### 🎯 When to Use

#### Automatic Activation
```bash
# Component creation
/sc:implement "modal component"  # Auto-activates Magic

# UI-specific keywords
/sc:build "responsive navigation"  # Auto-activates Magic
```

#### Manual Activation
```bash
# Force Magic for UI work
/sc:implement ui-feature --magic

# Design system integration
/sc:build component-library --magic --with-patterns
```

### 💡 Best Practices

#### Component Development
```bash
# Modern React component
/sc:implement "data table with sorting" --magic --framework react

# Vue 3 composition API
/sc:implement "form with validation" --magic --framework vue

# Responsive design
/sc:build "mobile-first layout" --magic --responsive
```

#### Design System Integration
```bash
# Use existing design tokens
/sc:implement components --magic --with-design-system

# Accessibility-first
/sc:build "accessible modal" --magic --focus accessibility
```

### 🎨 Component Categories

Magic handles:
- **Interactive**: Forms, modals, dropdowns
- **Layout**: Grids, containers, navigation
- **Display**: Cards, lists, tables
- **Feedback**: Alerts, toasts, loading states
- **Data**: Charts, graphs, visualizations

### 🔧 Advanced Usage

```bash
# Complex component systems
/sc:implement "dashboard with charts" --magic --all-components

# Animation and transitions
/sc:build "animated carousel" --magic --with-animations

# Cross-framework components
/sc:implement "web components library" --magic --framework agnostic
```

## Playwright - Browser Automation & Testing

### 🎭 Purpose
Cross-browser testing, E2E automation, and performance monitoring.

### 🎯 When to Use

#### Automatic Activation
```bash
# E2E testing
/sc:test e2e  # Auto-activates Playwright

# Performance testing
/sc:test performance --with-metrics  # Auto-activates Playwright
```

#### Manual Activation
```bash
# Force Playwright for testing
/sc:test user-flows --play

# Visual regression testing
/sc:test ui-changes --play --screenshot
```

### 💡 Best Practices

#### E2E Test Creation
```bash
# User workflow testing
/sc:test "checkout process" --play --type e2e

# Cross-browser testing
/sc:test compatibility --play --browsers all
```

#### Performance Monitoring
```bash
# Core Web Vitals
/sc:analyze performance --play --metrics cwv

# Load time analysis
/sc:test "page load speed" --play --performance
```

### 🎯 Testing Capabilities

Playwright provides:
- **Multi-Browser**: Chrome, Firefox, Safari, Edge
- **Mobile Testing**: Device emulation
- **Visual Testing**: Screenshots, comparisons
- **Performance**: Metrics, profiling
- **Accessibility**: WCAG compliance testing

### 🔧 Advanced Usage

```bash
# Parallel test execution
/sc:test all-features --play --parallel

# CI/CD integration
/sc:test regression-suite --play --ci-mode

# API and UI testing
/sc:test "full integration" --play --api --ui
```

## Server Coordination

### 🔄 Multi-Server Operations

#### Intelligent Combination
```bash
# Full-stack feature development
/sc:implement "user dashboard" --c7 --magic --seq
# Context7: Backend patterns
# Magic: UI components
# Sequential: Complex logic

# Comprehensive testing
/sc:test application --seq --play
# Sequential: Test planning
# Playwright: Test execution
```

#### All Servers Mode
```bash
# Maximum intelligence for complex tasks
/sc:analyze entire-system --all-mcp

# Selective disable for speed
/sc:analyze simple-file --no-mcp
```

### 📊 Server Selection Matrix

| Task Type | Primary Server | Secondary | When to Combine |
|-----------|---------------|-----------|-----------------|
| UI Development | Magic | Context7 | Framework-specific UI |
| API Development | Context7 | Sequential | Complex business logic |
| Debugging | Sequential | Playwright | UI-related bugs |
| Testing | Playwright | Sequential | Test strategy planning |
| Documentation | Context7 | Sequential | Complex explanations |

### 🎯 Coordination Patterns

#### Progressive Enhancement
```bash
# Start simple
/sc:implement feature

# Add servers as needed
/sc:implement feature --c7  # Add documentation
/sc:implement feature --c7 --magic  # Add UI generation
```

#### Domain-Specific Combinations
```bash
# Frontend full-stack
/sc:build "React app" --magic --c7 --play

# Backend with testing
/sc:implement "API with tests" --c7 --seq --play

# Analysis and documentation
/sc:analyze codebase --seq --c7
```

## Performance Optimization

### ⚡ Server Performance Tips

#### Selective Activation
```bash
# Use only needed servers
/sc:analyze backend-code --seq  # Skip UI servers

# Disable for simple tasks
/sc:explain "variable naming" --no-mcp
```

#### Caching Strategies
```bash
# Context7 caches documentation
/sc:implement "React hooks" --c7  # First call
/sc:implement "more React" --c7   # Cached, faster

# Sequential reuses analysis
/sc:analyze module --seq --cache
```

#### Parallel Processing
```bash
# Parallel server operations
/sc:analyze system --all-mcp --parallel

# Batched requests
/sc:test "multiple features" --play --batch
```

### 📈 Performance Metrics

| Server | First Call | Cached | Overhead |
|--------|------------|--------|----------|
| Context7 | 2-5s | <500ms | Low |
| Sequential | 3-7s | 1-2s | Medium |
| Magic | 1-3s | <1s | Low |
| Playwright | 5-10s | 2-5s | High |

## Troubleshooting

### 🔧 Common Issues

#### Server Timeout
```bash
# Issue: Server not responding
# Solution: Use fallback or retry
/sc:implement feature --c7 --timeout 30
/sc:implement feature --no-c7  # Fallback
```

#### Wrong Server Activation
```bash
# Issue: Unwanted server activating
# Solution: Explicitly disable
/sc:analyze code --no-magic  # Disable Magic
/sc:analyze code --only-seq  # Only Sequential
```

#### Performance Issues
```bash
# Issue: Slow operations
# Solution: Optimize server usage
/sc:analyze small-task --no-mcp  # Faster
/sc:analyze large-task --seq --cached  # Use cache
```

### 🛠️ Debugging Server Issues

```bash
# Enable server diagnostics
/sc:analyze code --debug-mcp

# Check server status
/sc:test mcp-servers --diagnose

# Force server refresh
/sc:analyze code --c7 --refresh
```

### 📋 Quick Fixes

| Problem | Solution | Command |
|---------|----------|---------|
| Timeout | Increase timeout | `--timeout 60` |
| Wrong patterns | Force refresh | `--c7 --refresh` |
| Slow performance | Disable servers | `--no-mcp` |
| Cache issues | Clear cache | `--clear-cache` |

## 🎯 Quick Reference

### Essential Flags
- **Context7**: `--c7` or `--context7`
- **Sequential**: `--seq` or `--sequential`
- **Magic**: `--magic`
- **Playwright**: `--play` or `--playwright`
- **All Servers**: `--all-mcp`
- **No Servers**: `--no-mcp`

### Auto-Activation Keywords
- **Context7**: import, require, framework names
- **Sequential**: debug, analyze, complex, think
- **Magic**: component, UI, responsive, design
- **Playwright**: test, E2E, performance, browser

### Best Practices Summary
1. Let auto-activation work first
2. Add servers progressively as needed
3. Disable servers for simple tasks
4. Use caching for repeated operations
5. Combine servers for complex tasks

Remember: MCP servers are powerful tools - use them wisely!
