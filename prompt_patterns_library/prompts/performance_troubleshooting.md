# Performance Troubleshooting Prompt Template

**Role**: Act as a performance-focused software engineer.

**Task**: Analyse the provided code and performance information to identify potential bottlenecks. Recommend changes only where there is a reasonable basis for expecting an improvement.

**Input Placeholder**: 
- Programming language: [LANGUAGE]
- Relevant code: [CODE_BLOCK]
- Observed performance problem: [PERFORMANCE_PROBLEM]
- Measurements or profiling results: [PERFORMANCE_DATA]
- Constraints: [CONSTRAINTS]

**Expected Output**: 
1. Potential bottlenecks and supporting evidence.
2. Recommended optimisations, prioritised by impact.
3. Example code changes where appropriate.
4. Suggestions for benchmarking before and after the changes.