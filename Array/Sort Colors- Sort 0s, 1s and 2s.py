'''
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

'''
import unittest
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012_broke(self, arr):
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

    def sort012(self, arr):
        low, mid, high = 0, 0, len(arr) - 1
        
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
                
        return arr

    
import unittest

class TestSort012(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        result = self.solution.sort012([])
        print(f"Input: [], Output: {result}, Passed: {result == []}")
        self.assertEqual(result, [])

    def test_single_element_array(self):
        result = self.solution.sort012([0])
        print(f"Input: [0], Output: {result}, Passed: {result == [0]}")
        self.assertEqual(result, [0])

        result = self.solution.sort012([1])
        print(f"Input: [1], Output: {result}, Passed: {result == [1]}")
        self.assertEqual(result, [1])

        result = self.solution.sort012([2])
        print(f"Input: [2], Output: {result}, Passed: {result == [2]}")
        self.assertEqual(result, [2])

    def test_sorted_array(self):
        result = self.solution.sort012([0, 1, 2])
        print(f"Input: [0, 1, 2], Output: {result}, Passed: {result == [0, 1, 2]}")
        self.assertEqual(result, [0, 1, 2])

    def test_reverse_sorted_array(self):
        result = self.solution.sort012([2, 1, 0])
        print(f"Input: [2, 1, 0], Output: {result}, Passed: {result == [0, 1, 2]}")
        self.assertEqual(result, [0, 1, 2])

    def test_mixed_array(self):
        result = self.solution.sort012([0, 2, 1, 2, 0, 1])
        print(f"Input: [0, 2, 1, 2, 0, 1], Output: {result}, Passed: {result == [0, 0, 1, 1, 2, 2]}")
        self.assertEqual(result, [0, 0, 1, 1, 2, 2])

        result = self.solution.sort012([2, 2, 1, 1, 0, 0])
        print(f"Input: [2, 2, 1, 1, 0, 0], Output: {result}, Passed: {result == [0, 0, 1, 1, 2, 2]}")
        self.assertEqual(result, [0, 0, 1, 1, 2, 2])

        result = self.solution.sort012([1, 0, 2, 1, 0, 2])
        print(f"Input: [1, 0, 2, 1, 0, 2], Output: {result}, Passed: {result == [0, 0, 1, 1, 2, 2]}")
        self.assertEqual(result, [0, 0, 1, 1, 2, 2])

if __name__ == '__main__':
    unittest.main()


