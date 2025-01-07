'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
from typing import List
#Neetcode Solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # If the current interval starts after the new interval ends
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # If the current interval ends before the new interval starts
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # Overlapping intervals; merge them
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # Add the merged interval at the end if not added earlier
        res.append(newInterval)
        return res
    
    def insert2(intervals, newInterval):
        result = []
        for interval in intervals:
            if interval[1] < newInterval[0]:  # New interval is right of the current interval
                result.append(interval)
            elif interval[0] > newInterval[1]:  # New interval is left of the current interval
                result.append(newInterval)
                newInterval = interval  # Update newInterval to the current one, as it's not inserted yet
            else:  # Overlapping intervals, merge them
                newInterval[0] = min(interval[0], newInterval[0])  # Take the min start time
                newInterval[1] = max(newInterval[1], interval[1])  # Take the max end time
        result.append(newInterval)  # Add the last interval, which might be merged or the original new interval
        return result


                
# Importing the Solution class
solution = Solution()

# Test Case 1: Overlapping intervals
print(solution.insert([[1, 3], [6, 9]], [2, 5]))
# Expected Output: [[1, 5], [6, 9]]

# Test Case 2: Non-overlapping, new interval before all
print(solution.insert([[4, 5], [7, 9]], [1, 2]))
# Expected Output: [[1, 2], [4, 5], [7, 9]]

# Test Case 3: Non-overlapping, new interval after all
print(solution.insert([[1, 2], [3, 5]], [6, 7]))
# Expected Output: [[1, 2], [3, 5], [6, 7]]

# Test Case 4: Fully overlapping an existing interval
print(solution.insert([[1, 5]], [2, 3]))
# Expected Output: [[1, 5]]

# Test Case 5: Overlapping multiple intervals
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10]], [4, 8]))
# Expected Output: [[1, 2], [3, 10]]

# Test Case 6: New interval spans all intervals
print(solution.insert([[2, 3], [5, 7]], [1, 8]))
# Expected Output: [[1, 8]]

# Test Case 7: Empty interval list
print(solution.insert([], [4, 8]))
# Expected Output: [[4, 8]]

# Test Case 8: Single interval with no overlap
print(solution.insert([[1, 2]], [3, 4]))
# Expected Output: [[1, 2], [3, 4]]

# Test Case 9: Exact match with an interval
print(solution.insert([[1, 2], [3, 4]], [3, 4]))
# Expected Output: [[1, 2], [3, 4]]


        