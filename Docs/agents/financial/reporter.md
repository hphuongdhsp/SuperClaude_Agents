# Agent: Reporter

## 🤖 Overview
**Department**: Financial
**Agent ID**: `reporter`
**Activation**: Use `Task` tool with `subagent_type="reporter"`
**Version**: SuperClaude v3

## 📋 Purpose
Generates comprehensive equity research reports for Vietnamese listed companies (HOSE, HNX, UPCOM). Produces detailed company research reports analyzing fundamentals, valuation, and investment thesis, saved to `/reports/{TICKER}_research_{YYYYMMDD}.md`.

## 🛠️ Core Capabilities
- **Primary Function**: Professional equity research report generation
- **Specializations**:
  - Vietnamese stock market analysis (HOSE, HNX, UPCOM)
  - Financial statement analysis and interpretation
  - Valuation modeling and peer comparison
  - Investment thesis development
  - Risk assessment and scenario analysis
- **Integration Points**: Works with financial data APIs, integrates with kols agent for macro context

## 🔧 Available Tools
This agent has access to the following tools:
- `Write` - Creates detailed research reports in markdown format
- `Read` - Analyzes existing reports and financial documents
- `WebSearch` - Researches company news, industry trends, and market data
- `WebFetch` - Retrieves financial data from web sources

## 🎯 Use Cases

### When to Use This Agent
- **Scenario 1**: Need comprehensive analysis of a Vietnamese listed company
- **Scenario 2**: Preparing investment committee presentations
- **Scenario 3**: Quarterly earnings analysis and updates
- **Scenario 4**: Sector comparison and peer analysis
- **Scenario 5**: IPO analysis and new listing evaluation

### When NOT to Use This Agent
- ❌ Real-time trading decisions (use market data tools instead)
- ❌ Non-Vietnamese markets (specialized for Vietnam only)
- ❌ Cryptocurrency or forex analysis

## 💡 Examples

### Example 1: Single Company Analysis
```
Context: Investor needs analysis of a Vietnamese bank
user: "Generate a research report for VCB (Vietcombank)"
assistant: "I'll use the reporter agent to create a comprehensive equity research report for VCB."
<uses Task tool with subagent_type="reporter">
```
**Outcome**: Detailed report saved to `/reports/VCB_research_20250201.md` with:
- Executive summary and investment thesis
- Financial performance analysis (5-year historical)
- Valuation analysis (P/E, P/B, DCF)
- Peer comparison with other banks
- Risk factors and catalysts
- Investment recommendation with target price

### Example 2: Sector Comparison
```
Context: Comparing multiple companies in the same sector
user: "Analyze and compare the top 3 Vietnamese steel companies: HPG, HSG, and NKG"
assistant: "I'll use the reporter agent to create a comparative analysis of the Vietnamese steel sector leaders."
<uses Task tool with subagent_type="reporter">
```
**Outcome**: Comparative report with sector overview, individual company analysis, and relative rankings

## 🔄 Integration Patterns

### Works Well With
- **kols agent**: Provides macro context and global market insights
- **trump agent**: Analyzes policy impacts on specific sectors/companies
- **trend-researcher**: Identifies market trends affecting valuations

### Common Workflows
1. **Comprehensive Investment Analysis**: kols (macro view) → **reporter** (company specific) → portfolio recommendations
   - Purpose: Complete top-down investment analysis
   - Example: Global monetary policy → Vietnam banks → specific bank picks

2. **Policy Impact Assessment**: trump (policy announcement) → **reporter** (affected companies) → investment adjustments
   - Purpose: Rapid response to policy changes
   - Example: New tariffs → steel company impact → HSG analysis update

## ⚙️ Configuration & Flags

### Auto-Activation
This agent may be automatically selected when:
- Keywords detected: `research report`, `equity analysis`, `VN30`, `HOSE`, `HNX`, `fundamental analysis`
- Context indicators: Vietnamese ticker symbols, financial ratios mentioned
- Project type: Investment research, portfolio management

### Performance Considerations
- **Speed**: Medium - Thorough analysis takes 10-15 minutes
- **Token Usage**: High - Comprehensive reports use 15-25K tokens
- **Complexity Handling**: Excels at complex financial analysis and modeling

## 📊 Best Practices

### Do's
✅ Provide specific ticker symbols for Vietnamese stocks
✅ Specify the depth of analysis needed (quick view vs. comprehensive)
✅ Include any specific concerns or focus areas
✅ Request updates to existing reports for efficiency

### Don'ts
❌ Don't expect real-time price data (use market terminals)
❌ Don't use for day trading decisions
❌ Don't rely solely on report without your own due diligence

## 🔍 Troubleshooting

### Common Issues
1. **Issue**: Cannot find financial data for ticker
   - **Solution**: Ensure ticker is correct and listed on HOSE/HNX/UPCOM

2. **Issue**: Report seems outdated
   - **Solution**: Request fresh analysis with current date parameter

3. **Issue**: Missing specific metrics
   - **Solution**: Explicitly request the metrics you need in the prompt

## 📚 Related Documentation
- [kols agent](./kols.md) - For macro market context
- [trump agent](./trump.md) - For policy impact analysis
- [trend-researcher agent](../product/trend-researcher.md) - For market trends
- [Financial Analysis Workflow Guide](../../guides/financial-analysis-workflow.md)

---
*Agent documentation for SuperClaude v3*
