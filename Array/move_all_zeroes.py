def move_zeroes(nums):
    """
    Move all zeroes to the end of the array while maintaining the relative order of non-zero elements.
    """
    non_zero_index = 0  # Index to track the position where the next non-zero element should go

    # Iterate through the array
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap the non-zero element with the element at the current non-zero index
            nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
            non_zero_index += 1  # Increment the non-zero index

    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))  # Output: [1, 3, 12, 0, 0]

## Relation to Quick Sort
'''
### 1. Partitioning Logic
This algorithm resembles the partitioning step of **Quick Sort**, where elements are rearranged based on a pivot.

- **In Quick Sort**:
  - Elements smaller than the pivot are moved to the left.
  - Elements larger than the pivot are moved to the right.

- **In this function**:
  - Non-zero elements act as "smaller" elements (moved to the left).
  - Zeros act as "larger" elements (moved to the right).

### 2. Two-Pointer Technique
Both this algorithm and Quick Sort's partition step use a **two-pointer approach**:
- `non_zero_index` functions like the left partition pointer in Quick Sort.
- `i` iterates through the array, similar to how Quick Sort scans elements for swapping.

### 3. In-Place Rearrangement
Like Quick Sort’s partitioning step, this algorithm operates **in-place** without needing extra space, making it space-efficient.

### Key Difference
- **Quick Sort** fully sorts the array.
- **This function** only partitions the array to move all zeros to the end, preserving the relative order of non-zero elements.
'''