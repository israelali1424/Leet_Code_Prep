# Bubble Sort in Python

## How Bubble Sort Works:
1. Compare adjacent elements.
2. Swap them if they are in the wrong order.
3. Repeat the process for the next pair of elements.
4. Continue this process for multiple passes until no swaps are needed.

## Python Code Example:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made
        swapped = False
        # Last i elements are already in place
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, break (array is sorted)
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
