---
paths:
  - "agents_complete_with_report.py"
---

# Data Processing Rules

When modifying tools or analysis functions in this file:

1. All tools return structured JSON only. Errors are wrapped in JSON, never raised as uncaught exceptions.
2. Tools are pure functions: same input produces identical output every time.
3. All numeric calculations include error handling for missing or malformed data.
4. Tool outputs are wrapped in tool_result blocks before being passed to Claude. Raw data never passes directly.
5. Each tool's description states clearly what it returns and what it does not, so tool selection stays unambiguous.