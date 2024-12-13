# Binary Search Algorithm

## Overview

- **Purpose**: Used for finding a target value within a sorted array efficiently.
- **Concept**: Repeatedly divides the search space in half by comparing the middle element with the target value.
- **Relation to Divide and Conquer**:  
  It is a classic divide-and-conquer algorithm, as it splits the problem into smaller subproblems.
- **Interview Relevance**:  
  A fundamental algorithm frequently tested in technical interviews and real-world applications.

## Complexity

- **Time Complexity**: O(log n) – Logarithmic time
- **Space Complexity**: 
  - O(1) – Constant space for iterative 
  - O(log n) – For recursive

## Key Requirements

- Array must be sorted
- Random access to elements (index-based access)

## Example Implementation
```
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)  # Returns 3 (index of target)
```