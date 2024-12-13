# Quick Sort Algorithm in Python

Quick Sort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

## Steps:

1. **Choose a Pivot**: Select an element from the array (e.g., the last element).
2. **Partition**: Rearrange the array so that all elements smaller than the pivot are on the left, and all larger elements are on the right.
3. **Recursion**: Recursively apply the same process to the left and right sub-arrays.

## Python Code:

```python
def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Select the pivot (we choose the last element in the array)
    pivot = arr[-1]

    # Partition the array into two sub-arrays: less than pivot and greater than pivot
    less_than_pivot = [x for x in arr[:-1] if x <= pivot]
    greater_than_pivot = [x for x in arr[:-1] if x > pivot]

    # Recursively sort the sub-arrays and combine the results with the pivot in between
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
```
