---
allowed-tools: [Read, Grep, Glob, LS]
description: "Generate comprehensive folder structure summaries with statistics and insights"
category: "analysis"
complexity: "moderate"
personas: ["analyzer", "architect"]
---

# /sc:summary - Folder Summary Generator

## Purpose
Analyze and summarize folder contents, providing insights into project structure, file distributions, code organization, and potential issues. Perfect for understanding new codebases or documenting project structure.

## Usage
```
/sc:summary @folder [--depth 2] [--include-sizes] [--format tree|list|report] [--focus code|docs|all]
```

## Arguments
- `@folder` - Target folder path to analyze (required)
- `--depth` - Maximum directory traversal depth (default: 2, range: 1-5)
- `--include-sizes` - Include file and directory sizes in summary
- `--format` - Output format:
  - `tree` - Tree-style visualization (default)
  - `list` - Flat list with categories
  - `report` - Detailed analysis report
- `--focus` - Analysis focus:
  - `code` - Focus on source code files
  - `docs` - Focus on documentation
  - `all` - Comprehensive analysis (default)

## Execution
1. Validate target folder exists and is accessible
2. Scan directory structure using LS with depth limit
3. Categorize files by type using Glob patterns
4. Calculate statistics (file counts, types, sizes if requested)
5. Identify notable patterns or potential issues
6. Generate formatted output based on selected format
7. Provide actionable insights and recommendations

## Claude Code Integration
- Uses LS for efficient directory traversal
- Applies Glob for intelligent file type detection
- Leverages Read for sampling file contents when needed
- Integrates Grep for pattern detection in large folders
- Maintains performance with automatic optimization for large directories

## Auto-Activation Patterns
- **Large folders** (>1000 files): Automatically enables --uc compression
- **Deep structures** (>5 levels): Suggests limiting depth for performance
- **Code-heavy folders**: Activates analyzer persona for code insights
- **Documentation folders**: Activates scribe persona for content analysis

## Performance Notes
- Optimized for folders up to 10,000 files
- Implements smart caching for repeated analysis
- Automatically adjusts strategy based on folder size
- Uses batched operations to minimize token usage

## Output Examples

### Tree Format (Default)
```
📁 src/ (423 files, 2.1MB)
├── 📁 components/ (156 files)
│   ├── 📁 common/ (45 files)
│   ├── 📁 features/ (89 files)
│   └── 📁 layouts/ (22 files)
├── 📁 utils/ (67 files)
├── 📁 services/ (43 files)
└── 📄 index.js

Summary: Primarily React components (37%), utilities (16%), services (10%)
Issues: Large components folder may benefit from reorganization
```

### Report Format
```
## Folder Analysis Report: src/

### Overview
- Total Files: 423
- Total Size: 2.1MB
- Directory Depth: 4 levels
- Last Modified: 2024-01-15

### File Distribution
1. JavaScript/JSX: 312 files (73.8%)
2. CSS/SCSS: 67 files (15.8%)
3. Tests: 38 files (9.0%)
4. Other: 6 files (1.4%)

### Key Insights
- Well-organized component structure
- Good test coverage (1:8 ratio)
- Consistent naming conventions

### Recommendations
1. Consider splitting large components folder
2. Add README files to key directories
3. Standardize test file locations
```

## Examples
```
# Basic folder summary
/sc:summary @src

# Deep analysis with sizes
/sc:summary @. --depth 3 --include-sizes

# Code-focused report format
/sc:summary @app --format report --focus code

# Quick documentation overview
/sc:summary @docs --depth 1 --focus docs

# Full project analysis
/sc:summary @. --depth 4 --format report --include-sizes
```

## Error Handling
- **Invalid path**: Provides clear error message and suggests valid paths
- **Permission denied**: Lists accessible portions and notes restrictions
- **Large folders**: Automatically optimizes or suggests sampling
- **Circular symlinks**: Detects and reports without infinite loops

## Future Enhancements
- Git integration for change history
- Technology stack detection
- Dependency analysis
- Code quality metrics
- Visual diagrams for complex structures