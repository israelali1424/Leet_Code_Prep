class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        if len(arr)<=1:
            return arr
        
        pivot = arr[-1]
        left = []
        right = []
        
        for number in arr[:-1]:
            if number >= pivot:
                right.append(number)
            else:
                left.append(number)
        return self.sort012(left) + [pivot] + self.sort012(right)
    
s= Solution()
# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = s.sort012(arr)
print("Sorted array:", sorted_arr)

# Example usage:
arr = [10, 7, 8, 9, 1, 5,10,100,0,4,5,443,54]
sorted_arr = s.sort012(arr)
print("Sorted array:", sorted_arr)