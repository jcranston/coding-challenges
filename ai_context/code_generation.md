# Code Generation Policy

## MANDATORY WORKFLOW - ALWAYS FOLLOW THIS ORDER

**CRITICAL: Before presenting ANY code to the user, you MUST complete this workflow:**

1. **Create/Edit the code** following project conventions
2. **Run `make quality`** - this runs format + lint + test
3. **Fix any issues** that `make quality` finds
4. **Only present code** after `make quality` passes completely
5. **If `make quality` fails, fix the issues and run it again**

**CRITICAL: NEVER present code without running `make quality` first. This is MANDATORY.**

**CRITICAL: If you cannot run `make quality` (e.g., in a restricted environment), manually:**
- Run `make format` 
- Run `make lint` and fix any errors
- Run `make test` to ensure tests pass
- Only then present the code

## Linter and Style Requirements

All generated Python code (including stubs, tests, explanations, scripts, comments, and docstrings) must comply with flake8 linter requirements. The AI should automatically fix any linter errors in generated code before presenting or committing it, without asking the user for confirmation.

**CRITICAL: Before presenting any code, manually verify that all lines respect the 80-character limit. Count characters or use a linter to check. This applies to function signatures, docstrings, and all other code.**

**CRITICAL: ALWAYS manually count characters in docstrings and function signatures before presenting code. This is the MOST COMMON ERROR and must be caught every time.**

**CRITICAL: ALWAYS check for W293 (blank line contains whitespace) before presenting code. This is the SECOND MOST COMMON ERROR. Remove any spaces/tabs from blank lines.**

**CRITICAL: ALWAYS ensure files end with a newline (W292) and have no trailing whitespace (W291).**

## File Creation and Formatting Requirements

**CRITICAL: When creating new files, ensure proper formatting:**
- Files must end with exactly one newline character
- No trailing whitespace on any line
- No spaces or tabs in blank lines
- Proper indentation (4 spaces, not tabs)
- Consistent spacing around operators and after commas

**CRITICAL: File ending requirements:**
- Every file must end with exactly one newline character
- No trailing whitespace on the last line
- Use `echo "" >> filename` or equivalent to ensure proper file endings

**CRITICAL: Blank line requirements:**
- Blank lines should contain no whitespace (spaces or tabs)
- Use `sed -i 's/[[:space:]]*$//' filename` to remove trailing whitespace
- Check for W293 errors before presenting code

**CRITICAL: Docstring formatting expectations:**
- Multi-line docstrings should wrap at 80 characters
- First line should be a brief summary
- Args/Returns sections should be properly indented
- Use consistent spacing and line breaks
- **CRITICAL: When implementing solutions, maintain the existing docstring format or use the format that will pass docformatter.**
- **CRITICAL: Single-line docstrings should remain single-line unless they exceed 80 characters.**
- **CRITICAL: Multi-line docstrings should follow the docformatter rules (--wrap-summaries 80 --wrap-descriptions 80).**
- Example format:
  ```python
  def function_name(param1: str, param2: int) -> bool:
      """Brief summary that wraps at 80 characters.
      
      Longer description if needed, also wrapped at 80 characters.
      
      Args:
          param1: Description of first parameter
          param2: Description of second parameter
          
      Returns:
          Description of return value
      """
  ```**

**CRITICAL: When referencing files or directories, always verify the exact path by checking the filesystem, including topic directories (e.g., `dynamic_programming/longest_common_subsequence`).**

**CRITICAL: Always run the linter before presenting code to catch W293 (blank line contains whitespace), E261 (missing spaces before comments), and other common errors.**

**CRITICAL: Do not automatically create commits unless the user explicitly asks for them. Present the changes and let the user decide when to commit.**

**CRITICAL: Use the improved test structure pattern for cleaner test files:**

```python
def assert_result(result, expected, method_name=""):
    """Helper function to check result and skip if not implemented."""
    if result is None:
        pytest.skip(f"Method {method_name} not implemented yet")
    assert result == expected

# Use this pattern instead of repetitive if result is None: continue blocks
assert_result(obj.method_call(), expected_value, "method_name")
```

**CRITICAL: For mathematical expressions in docstrings, comments, or documentation, use proper LaTeX notation (see `mathematical_formatting.md`).**

**CRITICAL: Debugging Methodology - Always investigate before making changes:**
- **Read files first** using `read_file` to see actual content
- **Use `grep`** to find exact patterns before attempting changes
- **Make targeted fixes** rather than multiple failed attempts
- **Verify changes** with `make quality` after each modification
- **Use `sed`** for precise line replacements when `search_replace` fails

**CRITICAL: Code formatting expectations:**
- Use consistent spacing around operators (e.g., `i - 1` not `i-1`)
- Use consistent spacing after commas in function calls and lists
- Break long lines at logical points (operators, commas)
- Use proper indentation for multi-line expressions
- Example format:

**CRITICAL: Solution file structure and docstring guidelines:**
- **DO NOT include module docstrings in solution.py files** - the README already contains all problem details, LeetCode references, and constraints
- **Solution files should focus purely on implementations** - avoid duplicating problem information
- **Keep function docstrings** as they provide valuable context about the specific approach and implementation details
- **Maintain clean separation of concerns**: README for problem description, solution.py for implementations, test_solution.py for verification
- **Function docstrings should explain**: what the function does, the approach being used, and any key implementation insights
  ```python
  result = max(
      rec_lcs(i - 1, j),  # skip char in text1
      rec_lcs(i, j - 1),  # skip char in text2
  )
  ```

### Critical Linting Rules (MUST FOLLOW)

**E501 - Line too long (max 80 characters):**
- Wrap long docstrings at word boundaries, preserving semantic meaning
- Break function signatures after opening parenthesis
- Split long import statements across multiple lines
- **CRITICAL**: When breaking docstrings, maintain semantic coherence - never break in the middle of a phrase or move just punctuation
- **CRITICAL**: Always manually verify line lengths before presenting code
- **Example of GOOD docstring breaking:**
```python
def function_name():
    """
    Brief description that gets too long and needs to be broken
    across multiple lines while maintaining semantic meaning.
    """
```
- **Example of BAD docstring breaking (DON'T DO THIS):**
```python
def function_name():
    """
    Brief description that gets too long and needs to be broken
    across multiple lines while maintaining semantic meaning
    .
    """
```
- **Example of function signature breaking:**
```python
def long_function_name(
    param1, param2, param3, param4, param5, 
    param6, param7, param8, param9, param10
):
```

**E302 - Expected 2 blank lines, found 0:**
- Add 2 blank lines after imports before function/class definitions
- Add 2 blank lines between function/class definitions
- Example:
```python
from typing import List


def function1():
    pass


def function2():
    pass
```

**E231 - Missing whitespace after comma:**
- Add space after commas in function calls, lists, tuples
- Example: `[1,2,3]` should be `[1, 2, 3]`

**E226 - Missing whitespace around arithmetic operator:**
- Add spaces around `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Example: `i+1` should be `i + 1`

**E261 - At least two spaces before inline comment:**
- Use at least 2 spaces before `#` comments
- Example: `x=1#comment` should be `x = 1  # comment`

**E302 - Expected 2 blank lines, found 0:**
- Add 2 blank lines after imports and between functions/classes

**W291 - Trailing whitespace:**
- Remove trailing spaces at end of lines

**W292 - No newline at end of file:**
- Ensure files end with a newline

**W293 - Blank line contains whitespace:**
- Remove any spaces/tabs from blank lines
- **CRITICAL: This is a very common error when generating code**

**CRITICAL: Import formatting expectations:**
- Imports should be sorted alphabetically
- Group standard library imports first, then third-party, then local
- Use consistent spacing and line breaks
- Example format:
  ```python
  import os
  import sys
  from pathlib import Path
  
  from typing import List, Optional
  
  from .solution import function_name
  ```

**W503 - Line break before binary operator:**
- Break lines after operators, not before

### IMPORTANT: Avoid Automated Sed Commands for E501

**CRITICAL WARNING**: When fixing E501 errors, avoid using broad automated `sed` commands that break lines at arbitrary character counts. These can create semantically broken code like:

```python
# BAD - Automated sed broke in the middle of a phrase
"""
The total number of good pairs (i, j) where nums[i] == nums[j] and
i < j.
"""

# BAD - Automated sed moved just punctuation
"""
The total number of good pairs (i, j) where nums[i] == nums[j] and i < j
.
"""
```

**CORRECT APPROACH**: Manually break lines at natural word boundaries while preserving semantic meaning:

```python
# GOOD - Manual break at word boundary
"""
The total number of good pairs (i, j) where nums[i] == nums[j] and i < j.
"""
```

### Code Generation Patterns

**Test Data:**
```python
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([1, 2, 3], 6),
        ([], 0),
        ([1], 1),
    ]
)
```

**Docstrings:**
```python
def function_name(param1: int, param2: str) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When invalid input is provided
    """
```

**Function Signatures:**
```python
def long_function_name(
    param1: List[int], 
    param2: Optional[str] = None
) -> Dict[str, Any]:
```

**Test Parameterization:**
```python
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
)
```

### IMPORTANT: Avoid Automated Sed Commands

- **NEVER** use automated `sed` commands to fix linting errors
- **ALWAYS** fix issues manually to preserve necessary blank lines and formatting
- **PRESERVE** the 2 blank lines required by E302
- **CHECK** the `.flake8` configuration for project-specific rules

### Project-Specific Configuration

The project uses `.flake8` with:
- `max-line-length = 80`
- `extend-ignore = E203,E235,F401,F811,E741`

**CRITICAL: Project Formatting Tools:**
- **docformatter**: Formats docstrings with `--wrap-summaries 80 --wrap-descriptions 80`
- **black**: Formats code with `line-length = 80`
- **isort**: Sorts imports with `profile = "black"`

**CRITICAL: When implementing solutions:**
1. **Maintain existing docstring format** - Don't change single-line to multi-line unnecessarily
2. **Follow docformatter rules** - If changing docstrings, ensure they pass docformatter
3. **Run `make format` after implementation** - To catch any formatting issues
4. **Check existing code style** - Match the formatting style of the existing codebase

**CRITICAL: Common Formatting Errors:**
- ❌ Changing single-line docstrings to multi-line unnecessarily
- ❌ Not following docformatter's 80-character wrap rules
- ❌ Inconsistent spacing in docstrings
- ❌ Not running `make format` after implementation

### Python Code Generation Guidelines (Black-Compatible)

**CRITICAL: When generating Python code, follow these Black-compatible patterns:**

#### Class Organization
```python
class MyClass:
    # 1. Constants (UPPER_CASE)
    DEFAULT_VALUE = 42
    MAX_SIZE = 100
    
    # 2. Inner classes
    class InnerClass:
        def __init__(self):
            pass
    
    # 3. Constructor
    def __init__(self, param: str = "default"):
        """Initialize the class.
        
        Args:
            param: Description of parameter
        """
        self.param = param
    
    # 4. Private helper methods (alphabetical, prefixed with _)
    def _calculate_something(self) -> float:
        """Calculate something.
        
        Returns:
            The calculated value
        """
        return 42.0
    
    # 5. Public interface methods (alphabetical)
    def clear(self) -> None:
        """Clear all data."""
        pass
    
    def get(self, key: Any) -> Optional[Any]:
        """Get value by key.
        
        Args:
            key: The key to look up
            
        Returns:
            The value or None if not found
        """
        pass
```

#### Import Organization
```python
# Standard library imports first
from typing import Optional, Any, List, Dict

# Third-party imports
import numpy as np

# Local imports
from .utils import helper_function
```

#### Variable Naming
- Use descriptive names
- Avoid shadowing built-ins (e.g., use `next_node` not `next`)
- Use consistent assignment spacing

#### Type Hints
- Always include type hints for function parameters and return values
- Use `Optional[Type]` for nullable values
- Use `Any` when type is truly unknown

#### Data Structures
- Use trailing commas in multi-line lists, dicts, tuples
- Break long lines at 88 characters (Black's default)
- Use consistent indentation

#### Error Handling
- Use specific exception types when possible
- Include meaningful error messages
- Re-raise exceptions when appropriate

### Application

This policy applies to all code generated for:
- New problems and solutions
- Test files and test data
- Documentation and explanations
- Project scripts and utilities
- README files and markdown content

Reference this file from any workflow or context file that involves code generation.