# These note are AI generated 
# Two Pointer Method

The two pointer method is a common algorithmic technique used to solve problems efficiently, especially in array, string, and linked list data structures. It involves using two pointers (or indices) to traverse the data structure and solve the problem in linear or near-linear time.

## Key Concepts
1. **Two Pointers:** Two variables that represent positions in the data structure.
2. **Direction:** The pointers can move:# Two Pointer Method

The two pointer method is a common algorithmic technique used to solve problems efficiently, especially in array, string, and linked list data structures. It involves using two pointers (or indices) to traverse the data structure and solve the problem in linear or near-linear time.

## Key Concepts
1. **Two Pointers:** Two variables that represent positions in the data structure.
2. **Direction:** The pointers can move:
   - In the **same direction** (e.g., both moving forward).
   - In **opposite directions** (e.g., one starting from the left and the other from the right).
3. **Use Cases:** The method is used when:
   - You need to find pairs or subsets with specific properties.
   - Problems can be reduced to smaller sub-problems by moving pointers.

## Common Patterns

### 1. **Opposite Direction Pointers**
   - **Scenario:** The pointers start at opposite ends of the array.
   - **Use Case:** Solving problems like finding pairs with a given sum in a sorted array.

#### Example: Two Sum in a Sorted Array
```python
# Given a sorted array, find two numbers that add up to a target.
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]  # Indices of the two numbers
        elif current_sum < target:
            left += 1  # Move left pointer to increase the sum
        else:
            right -= 1  # Move right pointer to decrease the sum

    return []  # No pair found
```

### 2. **Same Direction Pointers**
   - **Scenario:** Both pointers start from the same end and move in the same direction.
   - **Use Case:** Finding a subarray with specific properties, like the sliding window technique.

#### Example: Longest Substring Without Repeating Characters
```python
# Find the length of the longest substring without repeating characters.
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])# Two Pointer Method


## Advantages
- **Efficiency:** Reduces time complexity from O(n^2) to O(n) in many problems.
- **Simplicity:** Avoids unnecessary nested loops by using pointers.

## Limitations
- Requires the data structure to be sorted or have specific properties.
- Not always intuitive to implement, especially for beginners.

## Practice Problems
1. [Two Sum II - Input Array Is Sorted (LeetCode)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
2. [Container With Most Water (LeetCode)](https://leetcode.com/problems/container-with-most-water/)
3. [3Sum (LeetCode)](https://leetcode.com/problems/3sum/)
4. [Longest Substring Without Repeating Characters (LeetCode)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Conclusion
The two pointer method is a versatile and powerful approach for solving a wide variety of problems efficiently. Mastering this technique is crucial for excelling in technical interviews and competitive programming.
# Two Pointer Method

The two pointer method is a common algorithmic technique used to solve problems efficiently, especially in array, string, and linked list data structures. It involves using two pointers (or indices) to traverse the data structure and solve the problem in linear or near-linear time.

## Key Concepts
1. **Two Pointers:** Two variables that represent positions in the data structure.
2. **Direction:** The pointers can move:
   - In the **same direction** (e.g., both moving forward).
   - In **opposite directions** (e.g., one starting from the left and the other from the right).
3. **Use Cases:** The method is used when:
   - You need to find pairs or subsets with specific properties.
   - Problems can be reduced to smaller sub-problems by moving pointers.
