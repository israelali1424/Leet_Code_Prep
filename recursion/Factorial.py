# , denoted by. , is the product of all positive integers less than or equal to
# . For example, the factorial of is denoted by and is equal to .
#  example factorial of 5 is 5*4*3*2*1 = 120

class Solution():
    def factorial(self,n):
        if n==1:
            return 1
        return self.factorial(n) * self.factorial(n-1)
s = Solution()
print(s.factorial(2))