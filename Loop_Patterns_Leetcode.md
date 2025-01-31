# Loop Patterns in LeetCode Problems: A Guide

## FOR Loops: Fixed Pattern Traversal

### When to Use FOR Loops

- Known number of iterations
- Sequential traversal
- Fixed step size
- No need to manipulate iterator inside loop

### Common Problem Types and Examples

#### 1. Array/String Traversal

```python
# Problem: Find all palindromic substrings
def countPalindromes(s: str) -> int:
    count = 0
    for i in range(len(s)):
        # Odd length palindromes
        for j in range(len(s)):
            left, right = i - j, i + j
            if left < 0 or right >= len(s):
                break
            if s[left] != s[right]:
                break
            count += 1
    return count
```

#### 2. Matrix Problems

```python
# Problem: Island Perimeter
def islandPerimeter(grid: List[List[int]]) -> int:
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
```

## WHILE Loops: Dynamic Pattern Traversal

### When to Use WHILE Loops

- Unknown number of iterations
- Need to skip elements
- Multiple pointers moving at different speeds
- Complex stopping conditions
- Need to modify iterator inside loop

### Common Problem Types and Examples

#### 1. Two Pointer Problems

```python
# Problem: Container With Most Water
def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

#### 2. LinkedList Problems

```python
# Problem: Detect Cycle in LinkedList
def hasCycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False
```

#### 3. Stack/Queue Problems

```python
# Problem: Valid Parentheses
def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)

    return len(stack) == 0
```

## Common Patterns to Remember

### 1. Sliding Window

```python
# Use FOR when window size is fixed
def fixedWindow(arr: List[int], k: int) -> List[int]:
    result = []
    for i in range(len(arr) - k + 1):
        window = arr[i:i+k]
        result.append(max(window))
    return result

# Use WHILE when window size is dynamic
def dynamicWindow(arr: List[int], target: int) -> int:
    left = curr_sum = 0
    min_len = float('inf')

    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```

### 2. Binary Search

```python
# Almost always uses WHILE due to dynamic movement
def binarySearch(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## Tips for Choosing Between FOR and WHILE

1. Use FOR when:

   - You need to visit every element exactly once
   - The iteration pattern is straightforward
   - You know the exact number of iterations needed

2. Use WHILE when:
   - You might need to skip elements
   - You have multiple moving parts
   - The ending condition is complex
   - You need to modify the iterator inside the loop

Remember: When in doubt, consider whether you know exactly how many iterations you'll need. If yes, use FOR. If no, use WHILE.

I've created a comprehensive markdown guide that explains the patterns and provides concrete examples. Would you like me to explain any of the examples in more detail or add more specific cases?
