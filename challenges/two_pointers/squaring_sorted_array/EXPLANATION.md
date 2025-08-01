# Squares of a Sorted Array - Detailed Explanation

## Problem Recap

The Squares of a Sorted Array problem asks us to transform a sorted array of integers by squaring each element and returning the result in sorted order. This is a classic problem that tests understanding of array manipulation, sorting, and efficient algorithms.

**Key Constraints:**
- Input array is sorted in non-decreasing order
- Array length: 1 ≤ nums.length ≤ 10^4
- Element values: -10^4 ≤ nums[i] ≤ 10^4
- Output must be sorted in non-decreasing order

**Core Challenge:** The main difficulty lies in handling negative numbers, which become positive when squared and can disrupt the original sorted order.

## High-Level Approaches

There are three main approaches to solve this problem:

1. **Simple Approach**: Square all numbers, then sort (O(n log n))
2. **Two Pointers (Inward)**: Use two pointers moving inward from the ends (O(n))
3. **Binary Search + Two Pointers**: Find the vertex, then move outward (O(n))

The two pointers approaches are more efficient because they take advantage of the sorted nature of the input array.

## Step-by-Step Breakdown

### Approach 1: Simple Square and Sort

**Intuition:** Square all elements and then sort the result.

**Algorithm:**
1. Square each element in the array
2. Sort the squared values
3. Return the sorted result

**Time Complexity:** O(n log n) due to sorting
**Space Complexity:** O(n) for the result array

### Approach 2: Two Pointers (Inward)

**Intuition:** The largest squared values will be at the ends of the array, since negative numbers become positive when squared.

**Key Insight:** In a sorted array with negatives, the largest squares are at the extremes:
- Leftmost (most negative): `-4² = 16`
- Rightmost (most positive): `10² = 100`

**Algorithm:**
1. Initialize two pointers at the ends of the array
2. Compare squared values at both pointers
3. Place the larger squared value at the end of the result array
4. Move the pointer that contributed the larger value inward
5. Repeat until pointers meet

**Example:** `[-4, -1, 0, 3, 10]`
- Squared: `[16, 1, 0, 9, 100]`
- Compare 16 vs 100 → place 100 at end
- Compare 16 vs 9 → place 16
- Compare 1 vs 9 → place 9
- Compare 1 vs 0 → place 1
- Place 0 at beginning
- Result: `[0, 1, 9, 16, 100]`

### Approach 3: Binary Search + Two Pointers (Outward)

**Intuition:** Find the "vertex" (minimum squared value) using binary search, then build the result by moving outward.

**Key Insight:** The squared values form a V-shape, with the minimum at the vertex.

**Algorithm:**
1. Use binary search to find the vertex (minimum squared value)
2. Start from the vertex and move two pointers outward
3. Compare squared values and fill result in ascending order
4. Handle remaining elements on both sides

**Example:** `[-4, -1, 0, 3, 10]`
- Vertex is at index 2 (value 0, squared = 0)
- Start from vertex and move outward
- Result: `[0, 1, 9, 16, 100]`

## Annotated Code

### User Solution (Two Pointers Inward)

```python
def square_sorted_array_user(nums: list[int]) -> list[int]:
    """User's implementation of squaring sorted array.

    Square each number in the sorted array and return the result in sorted
    order.
    Handles negative numbers by squaring them (which makes them positive).

    Args:
        nums: Sorted array of integers in non-decreasing order

    Returns:
        Array of squared numbers in non-decreasing order
    """
    n = len(nums)
    result = [0] * n
    lp = 0
    rp = n - 1
    res_idx = n - 1

    while lp <= rp:  # <= ensures we handle the last element
        lval = nums[lp] ** 2
        rval = nums[rp] ** 2

        if lval < rval:
            result[res_idx] = rval
            rp -= 1
        else:
            result[res_idx] = lval
            lp += 1
        
        res_idx -= 1  # Fill from right to left (largest to smallest)
    
    return result
```

**Key Points:**
- Uses `<=` in loop condition to handle the case when pointers meet
- Fills result array from right to left (largest to smallest)
- Compares squared values to determine which pointer to move
- Time complexity: O(n), Space complexity: O(n)

### Canonical Solution (Two Pointers Inward)

```python
def square_sorted_array_canonical(nums: list[int]) -> list[int]:
    """Canonical implementation using two pointers technique.

    Square each number in the sorted array and return the result in sorted
    order.
    Uses two pointers to handle negative numbers efficiently by taking advantage
    of the sorted nature of the input array.

    Args:
        nums: Sorted array of integers in non-decreasing order

    Returns:
        Array of squared numbers in non-decreasing order
    """
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1  # Position to fill in result array

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1
        
        pos -= 1

    return result
```

**Key Points:**
- Cleaner variable names and structure
- Same logic as user solution but more readable
- Demonstrates the canonical approach for this problem

### Binary Search Solution (Alternative)

```python
def square_sorted_array_binary_search(nums: list[int]) -> list[int]:
    """Alternative canonical implementation using binary search to find vertex.

    First uses binary search to find the "vertex" (where squared values start
    increasing), then uses two pointers moving outward to build the result.

    Args:
        nums: Sorted array of integers in non-decreasing order

    Returns:
        Array of squared numbers in non-decreasing order
    """
    n = len(nums)
    if n == 0:
        return []
    
    result = [0] * n
    
    # Binary search to find the vertex (where squared values start increasing)
    left, right = 0, n - 1
    vertex = 0
    
    while left <= right:
        mid = (left + right) // 2
        if mid == 0 or nums[mid] ** 2 <= nums[mid - 1] ** 2:
            if mid == n - 1 or nums[mid] ** 2 <= nums[mid + 1] ** 2:
                vertex = mid
                break
            else:
                left = mid + 1
        else:
            right = mid - 1
    
    # Two pointers moving outward from the vertex
    left_ptr = vertex
    right_ptr = vertex
    pos = 0
    
    # Handle the vertex element first
    result[pos] = nums[vertex] ** 2
    pos += 1
    left_ptr -= 1
    right_ptr += 1
    
    # Move outward, comparing squared values
    while left_ptr >= 0 and right_ptr < n:
        left_square = nums[left_ptr] ** 2
        right_square = nums[right_ptr] ** 2
        
        if left_square <= right_square:
            result[pos] = left_square
            left_ptr -= 1
        else:
            result[pos] = right_square
            right_ptr += 1
        pos += 1
    
    # Handle remaining elements on the left
    while left_ptr >= 0:
        result[pos] = nums[left_ptr] ** 2
        left_ptr -= 1
        pos += 1
    
    # Handle remaining elements on the right
    while right_ptr < n:
        result[pos] = nums[right_ptr] ** 2
        right_ptr += 1
        pos += 1
    
    return result
```

**Key Points:**
- Uses binary search to find the vertex (minimum squared value)
- Two pointers move outward from the vertex
- Fills result in ascending order (smallest to largest)
- Handles edge cases properly (empty array)
- Demonstrates an alternative algorithmic approach

## Test Case Analysis

Let's examine key test cases to understand the patterns:

**Case 1: `[-4, -1, 0, 3, 10]` → `[0, 1, 9, 16, 100]`**
- Squared: `[16, 1, 0, 9, 100]`
- Two pointers: Compare 16 vs 100 → 100, 16 vs 9 → 16, 1 vs 9 → 9, 1 vs 0 → 1, 0
- Binary search: Vertex at index 2 (value 0), move outward

**Case 2: `[-7, -3, 2, 3, 11]` → `[4, 9, 9, 49, 121]`**
- Squared: `[49, 9, 4, 9, 121]`
- Two pointers: Compare 49 vs 121 → 121, 49 vs 9 → 49, 9 vs 9 → 9, 9 vs 4 → 9, 4

**Case 3: `[1, 2, 3, 4, 5]` → `[1, 4, 9, 16, 25]`**
- All positive numbers, order preserved after squaring
- Simple case where no reordering is needed

**Case 4: `[-5, -4, -3, -2, -1]` → `[1, 4, 9, 16, 25]`**
- All negative numbers, complete reversal after squaring
- Demonstrates the extreme case of negative number handling

## Common Pitfalls

1. **Incorrect loop condition**: Using `lp < rp` instead of `lp <= rp`
   - **Solution**: Use `<=` to handle the case when pointers meet

2. **Missing pointer updates**: Forgetting to update `res_idx` in the loop
   - **Solution**: Always decrement `res_idx` in each iteration

3. **Simple square-and-sort approach**: Using O(n log n) solution
   - **Solution**: Use two pointers for O(n) time complexity

4. **Binary search edge cases**: Not handling empty arrays or single elements
   - **Solution**: Add explicit checks for edge cases

5. **Incorrect vertex finding**: Binary search logic for finding the vertex
   - **Solution**: Carefully implement the binary search conditions

6. **Memory issues**: Creating unnecessary intermediate arrays
   - **Solution**: Square values inline when possible

## Variations and Extensions

1. **Grid with Obstacles**: Apply the same concept to 2D grid pathfinding
   - **Solution**: Use dynamic programming with similar two pointers logic

2. **Weighted Squares**: Each element has a weight that affects the squared value
   - **Solution**: Modify the squaring operation to include weights

3. **Custom Sorting**: Sort by different criteria after squaring
   - **Solution**: Modify the comparison logic in the two pointers approach

4. **In-Place Modification**: Modify the input array instead of creating a new one
   - **Solution**: Use the same two pointers logic but modify in place

5. **Streaming Data**: Handle arrays that are too large to fit in memory
   - **Solution**: Use external sorting or streaming algorithms

6. **Multiple Arrays**: Square and merge multiple sorted arrays
   - **Solution**: Extend the two pointers approach to multiple arrays

## Relevant Literature and Resources

1. **LeetCode Problem #977**: The original problem
   - https://leetcode.com/problems/squares-of-a-sorted-array/

2. **Two Pointers Technique**:
   - "Introduction to Algorithms" (CLRS) - Chapter on array algorithms
   - Classic technique for sorted array problems

3. **Binary Search Variations**:
   - "Competitive Programming Handbook" by Antti Laaksonen
   - Binary search for finding local minima/maxima

4. **Array Manipulation**:
   - "Programming Pearls" by Jon Bentley
   - Chapter on array algorithms and efficient sorting

5. **Related Problems**:
   - Merge Sorted Arrays
   - Remove Duplicates from Sorted Array
   - Two Sum in Sorted Array
   - Container With Most Water

6. **Mathematical Properties**:
   - Properties of squared numbers and their ordering
   - Relationship between negative/positive numbers and their squares

## Time and Space Complexity

**Simple Approach (Square and Sort):**
- Time: O(n log n) - dominated by sorting
- Space: O(n) - result array

**Two Pointers Approach:**
- Time: O(n) - single pass through the array
- Space: O(n) - result array

**Binary Search Approach:**
- Time: O(n) - binary search O(log n) + two pointers O(n)
- Space: O(n) - result array

The two pointers approaches are more efficient than the simple square-and-sort method, especially for large arrays. The binary search approach, while more complex, demonstrates how different algorithmic techniques can be combined effectively.

## Key Insights for Interview Preparation

1. **Recognize the pattern**: When you see a sorted array with potential negative numbers, think about how operations affect the ordering.

2. **Two pointers is often optimal**: For sorted array problems, two pointers frequently provide O(n) solutions.

3. **Consider edge cases**: Empty arrays, single elements, all positive, all negative.

4. **Multiple approaches**: Be prepared to discuss different solutions and their trade-offs.

5. **Efficiency matters**: Avoid O(n log n) solutions when O(n) is possible.

This problem is excellent for testing understanding of array manipulation, algorithmic thinking, and efficient problem-solving techniques. 