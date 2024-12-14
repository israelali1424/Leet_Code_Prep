# Merge Sort Algorithm Explanation

Merge sort is a divide-and-conquer algorithm that recursively divides a list into smaller sublists until each sublist contains a single element, then merges these sublists to produce a sorted result.

## Algorithm Steps
1. **Divide**: Split the input array into two halves.
2. **Recursion**: Recursively sort the two halves.
3. **Merge**: Merge the sorted halves to create a fully sorted array.

## Implementation
```python
def merge_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        mid = length // 2
        left_half = merge_sort(sequence[:mid])
        right_half = merge_sort(sequence[mid:])
        
        result = []
        left_index = right_index = 0
        
        # Merge the sorted halves
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                result.append(left_half[left_index])
                left_index += 1
            else:
                result.append(right_half[right_index])
                right_index += 1
        
        # Add remaining elements from left half if any
        while left_index < len(left_half):
            result.append(left_half[left_index])
            left_index += 1
        
        # Add remaining elements from right half if any
        while right_index < len(right_half):
            result.append(right_half[right_index])
            right_index += 1
            
        return result
```

## Step-by-Step Example

Let's sort the array `[38, 27, 43, 3]`:

### Division Phase:
```
                [38, 27, 43, 3]
                /            \
         [38, 27]            [43, 3]
         /      \            /      \
      [38]      [27]      [43]      [3]
```

### Merge Phase:
```
      [38]      [27]      [43]      [3]
         \      /            \      /
         [27, 38]            [3, 43]
              \                /
             [3, 27, 38, 43]
```

### How the Merge Works
1. Compare the first elements of both halves.
2. Take the smaller element and add it to the result.
3. Move to the next element in the list where we took the smaller element.
4. Repeat until one list is empty.
5. Add all remaining elements from the non-empty list.

#### Example merging `[27, 38]` and `[3, 43]`:
- Compare 27 and 3: Add 3 to result `[3]`.
- Compare 27 and 43: Add 27 to result `[3, 27]`.
- Compare 38 and 43: Add 38 to result `[3, 27, 38]`.
- Add remaining 43 to result `[3, 27, 38, 43]`.

## Time Complexity
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

## Space Complexity
- O(n)

## Advantages and Disadvantages

### Advantages:
- Stable sorting algorithm (maintains relative order of equal elements).
- Guaranteed O(n log n) performance.
- Works well for linked lists.
- Predictable performance.

### Disadvantages:
- Requires extra space O(n).
- For small lists, might be slower than simpler algorithms like insertion sort.
- More memory writes than quicksort.

## When to Use Merge Sort
Merge sort is particularly useful when:
- You need stable sorting.
- You're working with linked lists.
- You need guaranteed O(n log n) performance.
- External sorting (sorting data that doesn't fit in memory).

Merge sort is often used as the underlying algorithm in various programming languages' built-in sorting functions, especially when stability is required.


** Notes made by Claude ai** 