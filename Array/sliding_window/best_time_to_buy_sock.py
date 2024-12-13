from typing import List

# broken code 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            umpire 
            the subarray is continoues 
            the sub array can be of anysize 
            Return the maximum profit you can achieve
            can the array be empty or only element handle that

            match 
            Slding window Question 
            array question
            Plan:
            have max_profit var set to [zero] by deafult
            in the loop have a running totl var 
            Hadle if price is size 1 or empety
            prices = [10,1,5,6,7,1]
            have to index 0starts 
            have another index start at 2 
            [10,1] Buy at 10 sell at one = profit = -9
            so if end- start > max_profit:
            start +1
            end +1 
            [1,5,6,7,1]
            start +1 = 1 
            end +1 = 5 
            [5-1] = 4 
            4 >0 sum >4 max_profit max_profit = sum 
            end+1 
            [1,6]
            end+ =1 
            end = 6  6-1 = 5 5>4 sum   max_profit max_profit = sum 
            [1,7] 7 -1 = 6  6>5 sum   max_profit max_profit = sum 
            end +1 
            [1,1]
            start = 1 
            end = 1   1 < 7 sum 
            start +1
            end +1  
            end > len(prices)
            break 
            return max profit 
        '''
        
        max_profit = 0 
        if (prices) >= 1:
            return 0 
        start = 0
        end = 1 
        while end > len(prices):
            total_sum = prices[end] - prices[start]
            if total_sum < max_profit:
                 max_profit = total_sum 
                 end+=1 
            else:
                start+=1
                end+=1 
        return max_profit

from typing import List
# fixed version of my code 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        start = 0       # Tracks the minimum buy price index
        end = 1         # Tracks the sell price index
        max_profit = 0  # Initialize max profit to 0

        while end < len(prices):
            # Calculate the profit if we sell at 'end'
            profit = prices[end] - prices[start]

            # Update max profit if the current profit is higher
            if profit > max_profit:
                max_profit = profit

            # If the current price at 'end' is lower than the price at 'start',
            # update 'start' to 'end' (new potential buy point)
            if prices[end] < prices[start]:
                start = end

            # Move the end pointer to the next position
            end += 1
        
        return max_profit

# working solution 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l: buy pointer, r: sell pointer
        maxP = 0     # Initialize max profit to 0

        while r < len(prices):
            if prices[l] < prices[r]:  # Profit can be made
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:  # Update buy pointer if current price is lower
                l += 1
            
            # Always move the sell pointer forward
            r += 1
        
        return maxP
