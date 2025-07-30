# Two Sum II - Input Array Is Sorted: Detailed Explanation

## Problem Overview

This is a variation of the classic Two Sum problem with a crucial constraint: **the input array is sorted in non-decreasing order**. This constraint allows us to use a more efficient approach than the original Two Sum problem.

## Key Insights

### 1. **Sorted Array Advantage**
- When an array is sorted, we can use **two pointers** technique
- Elements at the beginning are smaller, elements at the end are larger
- This gives us a systematic way to explore pairs

### 2. **Two Pointers Strategy**
- Start with pointers at opposite ends: `left = 0`, `right = len(numbers) - 1`
- Compare the sum of elements at these positions with the target
- Move pointers based on the comparison:
  - If `sum > target`: Move `right` pointer left (decrease sum)
  - If `sum < target`: Move `left` pointer right (increase sum)
  - If `sum == target`: Found the solution!

## Algorithm Analysis

### Time Complexity: O(n)
- Each pointer moves at most n times
- In the worst case, we traverse the array once
- Much better than O(n²) brute force approach

### Space Complexity: O(1)
- Only using a constant number of variables
- No extra data structures needed

## Step-by-Step Walkthrough

Let's trace through an example: `numbers = [2, 7, 11, 15]`, `target = 9`

```
Initial state:
left = 0, right = 3
numbers[left] = 2, numbers[right] = 15
sum = 2 + 15 = 17

Step 1: sum (17) > target (9)
- Move right pointer left: right = 2
- numbers[left] = 2, numbers[right] = 11
- sum = 2 + 11 = 13

Step 2: sum (13) > target (9)
- Move right pointer left: right = 1
- numbers[left] = 2, numbers[right] = 7
- sum = 2 + 7 = 9

Step 3: sum (9) == target (9) ✓
- Found solution: [left + 1, right + 1] = [1, 2]
```

## Implementation Details

### User's Solution Analysis

```python
def two_sum_sorted_user(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    sum = numbers[left] + numbers[right]

    while sum > target:
        right -= 1
        sum = numbers[left] + numbers[right]

    while sum < target:
        left += 1
        sum = numbers[left] + numbers[right]

    return [left + 1, right + 1]
```

**Strengths:**
- Simple and intuitive approach
- Directly implements the two pointers strategy
- Handles the 1-indexed requirement correctly

**Potential Issues:**
- Doesn't handle edge cases (empty array, single element)
- Could be more explicit about the while loop conditions

### Canonical Solution Analysis

```python
def two_sum_sorted_canonical(numbers: list[int], target: int) -> list[int]:
    if not numbers or len(numbers) < 2:
        return []

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
```

**Strengths:**
- Handles edge cases properly
- More explicit about the three cases (equal, less, greater)
- Clearer logic flow with if-elif-else structure
- Includes safety check for array bounds

## Why This Approach Works

### 1. **Monotonicity Property**
- Since the array is sorted, we know that `numbers[i] <= numbers[j]` for all `i < j`
- This means we can make informed decisions about which pointer to move

### 2. **Guaranteed Solution**
- The problem guarantees exactly one solution exists
- This means we don't need to handle cases where no solution is found
- The algorithm will always terminate with a valid result

### 3. **Optimality**
- We can't do better than O(n) because we need to potentially examine all elements
- The two pointers approach achieves this optimal complexity

## Common Mistakes to Avoid

### 1. **Forgetting 1-indexed Requirement**
```python
# Wrong
return [left, right]

# Correct
return [left + 1, right + 1]
```

### 2. **Incorrect Pointer Movement**
```python
# Wrong - moving wrong pointer
if current_sum < target:
    right -= 1  # This decreases the sum further!

# Correct
if current_sum < target:
    left += 1   # This increases the sum
```

### 3. **Not Handling Edge Cases**
```python
# Missing edge case handling
def solve(numbers, target):
    left, right = 0, len(numbers) - 1
    # What if numbers is empty or has only one element?
```

## Interview Tips

### 1. **Start with Brute Force**
- Mention that a brute force O(n²) solution is possible
- Then explain how the sorted constraint allows optimization

### 2. **Explain the Intuition**
- "Since the array is sorted, we can use two pointers..."
- "We start from the ends and work our way in..."

### 3. **Discuss Trade-offs**
- Time vs. space complexity
- When this approach is better than hash table approach
- Limitations of the sorted constraint requirement

### 4. **Handle Follow-up Questions**
- What if the array wasn't sorted?
- What if we needed to find all pairs?
- What if we needed to find the closest sum?

## Related Problems

- **Two Sum (LeetCode #1)**: Original problem with unsorted array
- **Three Sum (LeetCode #15)**: Extension to three numbers
- **Container With Most Water (LeetCode #11)**: Another two pointers problem
- **Valid Palindrome (LeetCode #125)**: Two pointers on string

## Practice Recommendations

1. **Implement both solutions** and compare their behavior
2. **Trace through examples** step by step
3. **Practice edge cases**: empty array, two elements, all same values
4. **Try variations**: find closest sum, find all pairs
5. **Compare with hash table approach** for unsorted arrays

This problem is excellent for practicing the two pointers technique and understanding how constraints can lead to more efficient solutions. 