'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
from typing import List
# my orginal solution wrong approach failed every test case
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Input: temperatures = [73,74,75,71,69,72,76,73]
        Output: [1,1,4,2,1,1,0,0]
        create a list to hold the new values 
        create index for current index
        create an index count lower temp 

        while index < len(temps):
        current_index = index 
        if temp[current_index] > temp[index]:
        lower_days +=1

        just do two nested for loops that most effect way I can think of 
        if index[j] < index[j+1] :
        lower_day+=1 
        else:
        stack.append[lower_days)
        lower_days = 0 
        break 
        '''
        stack = []
        lower_days = 0 

        for i in range(0,len(temperatures)):
            lower_temps = 0 
            for j in range(i+1,len(temperatures)):
                if  temperatures[j]> temperatures[i]:
                    print(f'{temperatures[j]}> {temperatures[i]}')
                    #result[i] = j - i  # Set the number of days to wait
                    stack.append(j-i)
                    break 
                else:
                    lower_temps+=1
            #stack.append(lower_temps)
        #stack.append(0)
        print(stack)
        return stack
    # brtue force solution failed time limit exceeded
    def dailyTemperatures_brute(self, temperatures: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    stack.append(j - i)
                    break
            else:  # This else belongs to the for loop - runs if no break occurred
                stack.append(0)
                
        return stack
    from typing import List


    def dailyTemperatures_optimized(self, temperatures: List[int]) -> List[int]:
        stack = []  # This will hold the indices of the temperatures list
        result = [0] * len(temperatures)  # Result list initialized to 0 for each day
        
        for i in range(len(temperatures)):
            # Pop elements from the stack while current temp is higher than stack's top temp
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()  # Get the index of the temperature
                result[idx] = i - idx  # Calculate the number of days to wait for a warmer temp

            stack.append(i)  # Append the current index to the stack

        return result
    
#Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with varying temperatures
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = solution.dailyTemperatures_optimized(temperatures1)
    print("Test Case 1:", result1, "Passed" if result1 == [1, 1, 4, 2, 1, 1, 0, 0] else "Failed")
    assert result1 == [1, 1, 4, 2, 1, 1, 0, 0]
    # Expected Output: [1, 1, 4, 2, 1, 1, 0, 0]

    # Test Case 2: All temperatures are the same
    temperatures2 = [30, 30, 30, 30, 30]
    result2 = solution.dailyTemperatures_optimized(temperatures2)
    print("Test Case 2:", result2, "Passed" if result2 == [0, 0, 0, 0, 0] else "Failed")
    assert result2 == [0, 0, 0, 0, 0]
    # Expected Output: [0, 0, 0, 0, 0]

    # Test Case 3: Temperatures are in descending order
    temperatures3 = [90, 80, 70, 60, 50]
    result3 = solution.dailyTemperatures_optimized(temperatures3)
    print("Test Case 3:", result3, "Passed" if result3 == [0, 0, 0, 0, 0] else "Failed")
    assert result3 == [0, 0, 0, 0, 0]
    # Expected Output: [0, 0, 0, 0, 0]

    # Test Case 4: Temperatures are in ascending order
    temperatures4 = [50, 60, 70, 80, 90]
    result4 = solution.dailyTemperatures_optimized(temperatures4)
    print("Test Case 4:", result4, "Passed" if result4 == [1, 1, 1, 1, 0] else "Failed")
    assert result4 == [1, 1, 1, 1, 0]
    # Expected Output: [1, 1, 1, 1, 0]


    # Test Case 5: Single temperature
    temperatures5 = [75]
    result5 = solution.dailyTemperatures_optimized(temperatures5)
    print("Test Case 5:", result5, "Passed" if result5 == [0] else "Failed")
    assert result5 == [0]
    # Expected Output: [0]

    # Test Case 6: Mixed temperatures with no warmer days
    temperatures6 = [80, 79, 78, 77, 76]
    result6 = solution.dailyTemperatures_optimized(temperatures6)
    print("Test Case 6:", result6, "Passed" if result6 == [0, 0, 0, 0, 0] else "Failed")
    assert result6 == [0, 0, 0, 0, 0]
    # Expected Output: [0, 0, 0, 0, 0]

    # Test Case 7: Mixed temperatures with some warmer days
    temperatures7 = [70, 71, 72, 68, 69, 75, 74, 73]
    result7 = solution.dailyTemperatures_optimized(temperatures7)
    print("Test Case 7:", result7, "Passed" if result7 == [1, 1, 3, 1, 1, 0, 0, 0] else "Failed")
    assert result7 == [1, 1, 3, 1, 1, 0, 0, 0]
    # Expected Output: [1, 1, 3, 1, 1, 0, 0, 0]