'''
Valid Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.
'''
#My Solution and it worked  I did not need help on this one 
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Create a hashmap of all the vaild possbile a pairs 
        A stack could be used to slove this question 
        if the list is empty that means you have a vaild input else false
        you loop through the list of elemnts  for each elments 
        if the value is in valils.pairs.key. Append to the list 
        if the value is in vaild.pairs value and == list.pop/ list[-1] and the list exist 
        pop item form the list else return False 
        fianl return true 
        '''
        pairs = {"(":")","{":"}","[":"]"}
        print(pairs)
        to_pop = []
        for char in s:
            if char in pairs.keys():
                to_pop.append(pairs[char])
            elif char in pairs.values() and to_pop and to_pop[-1] == char:
                to_pop.pop()
            else: 
                return False

        return to_pop == []