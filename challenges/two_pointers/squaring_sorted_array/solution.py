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

    while lp <= rp:
        lval = nums[lp] ** 2
        rval = nums[rp] ** 2

        if lval < rval:
            result[res_idx] = rval
            rp -= 1
        else:
            result[res_idx] = lval
            lp += 1

        res_idx -= 1

    return result


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
