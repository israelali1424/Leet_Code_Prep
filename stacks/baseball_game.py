'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
'''
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for op in operations:
            if op.lstrip('-').isnumeric() :
                score_stack.append(int(op))

            elif op =="+":
                prev_score =  score_stack.pop()
                prev_prev_score = score_stack.pop()
                new_score =  prev_prev_score + prev_score
                score_stack.append(prev_prev_score)
                score_stack.append(prev_score)
                score_stack.append(new_score)
            elif op =="D": 
                prev_score =  score_stack.pop()
                new_score = prev_score * 2
                score_stack.append(prev_score)
                score_stack.append(new_score)

            elif op == "C":
                score_stack.pop()

        print(score_stack)
        return sum(score_stack)

# Time Complexity: O(n), where n is the number of operations. Each operation is processed in constant time.
# Space Complexity: O(n), where n is the number of operations. In the worst case, all operations are numeric and stored in the stack.

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Regular case with all operations
    operations1 = ["5", "2", "C", "D", "+"]
    result1 = solution.calPoints(operations1)
    print("Test Case 1:", result1, "Passed" if result1 == 30 else "Failed")
    assert result1 == 30
    # Expected Output: 30

    # Test Case 2: Only numeric operations
    operations2 = ["1", "2", "3", "4"]
    result2 = solution.calPoints(operations2)
    print("Test Case 2:", result2, "Passed" if result2 == 10 else "Failed")
    assert result2 == 10
    # Expected Output: 10


    # Test Case 4: Only "D" operations
    operations4 = ["5", "D", "D", "D"]
    result4 = solution.calPoints(operations4)
    print("Test Case 4:", result4, "Passed" if result4 == 75 else "Failed")
    assert result4 == 75
    # Expected Output: 75