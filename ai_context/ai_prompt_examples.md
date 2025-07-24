# AI Prompt Examples

This file contains example prompts for using AI tools (Cursor, Copilot, ChatGPT, etc.) with this project. Use these as templates to get consistent, high-quality results.

## General Guidance
- Reference the relevant context file in your prompt (e.g., "Follow the steps in ai_context/new_problem.md").
- Be explicit about the workflow or convention you want the AI to follow.
- If you want to automate a multi-step process, ask the AI to follow the context files step by step.

## Example Prompts

### Adding a New Problem
```
Please add a new problem called 'maximum_product_subarray'.
Follow the steps in ai_context/new_problem.md and use the conventions in ai_context/tagging_and_readme.md.
```

### Updating Tags
```
Regenerate the tags.md file by reading all problem READMEs and following the rules in ai_context/tagging_and_readme.md.
```

### Linting and Testing
```
Run the linter and all tests for the problem in arrays/maximum_subarray. Fix any issues according to the conventions in ai_context/tagging_and_readme.md.
```

### Custom Workflow
```
I want to add a new dynamic programming problem and have it fully tagged, tested, and documented. Please follow all steps in ai_context/new_problem.md and ai_context/tagging_and_readme.md.
```

## For AI Assistants
- Always check for a relevant context file before starting a workflow.
- If the user does not specify a file, ask if there is a context file you should follow.
- If you are unsure about a step, ask the user or refer to the context files in this directory.

## For Users
- Use these example prompts to get the most out of AI tools.
- Update this file with new prompt examples as your workflows evolve. 