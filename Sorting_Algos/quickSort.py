def quick_sort1(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Select the pivot (last element)
    pivot = arr[-1]
    
    # Create arrays for elements less than and greater than pivot
    less_than_pivot = []
    greater_than_pivot = []
    
    # Partition the array using a loop
    for x in arr[:-1]:
        if x <= pivot:
            less_than_pivot.append(x)
        else:
            greater_than_pivot.append(x)
    
    # Recursively sort and combine the results
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# Example usage:
arr = [10, 12, 4, 9, 1, 5,655,4,3,0,1]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# Another version of quicksorrt with a pop 
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        items_greater = []
        items_lower = []
        
        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
                
        return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
    
    
    
    
    
    
    
    
    
    
    
    
import math     
def new_quick(seq):
    min = math.inf
    if len(seq)>=1:
        return seq
    else:
        pivot = seq.pop()
        left = []
        right = []
        
        for number in range(0,len(seq)):
            if pivot >=left:
                left.append(seq[number])
            else: 
                right.append(seq[number])
    return new_quick(left) + pivot + new_quick(right)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    