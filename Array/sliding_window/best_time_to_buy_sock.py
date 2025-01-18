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
# approach 2 1/18/2025 
'''
I put a 20 minute timer finshed in about 18 minutes
I was able to solve the problem but not effeciently. I did not recgoinze the sliding window pattern fully
I knew it was possbile but I could think of way to slove the progblem using that method in the time frame. So
I did the brute force solution that came to mind and throught I could optimize it later. I nevver got optimize it.
But this what I have below 
'''
class Solution_Two: # very slow runtine 223ms and beats 5.04 
    def maxProfit(self, prices: List[int]) -> int:
        '''
        creat a var max_profit
        buy_date = None
        SellDate = None
        start loop
        for day_price in prices:
        if not buy_price:
        buy_price = day_price
        elif day_price < buy_price:
        buy_price = day_price

        if day_Price > buy_price:
        diff = day_pirce - buy_price
        max_profit = max (max_profit,diff)

        return max_profit
        '''
        max_profit = 0
        buy_price = None 

        for price in prices:
            if buy_price is None:
                buy_price = price 
                print(price)
            elif price <buy_price:
                buy_price = price 
                print(buy_price)
            elif  price > buy_price:
                profit = price - buy_price
                print(profit) 
                max_profit = max(max_profit, profit)

        return max_profit 

# Test Cases
if __name__ == "__main__":
    solution = Solution_Two()
    
    # Test Case 1: Regular case with profit
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(prices1)
    print("Test Case 1:", result1, "Passed" if result1 == 5 else "Failed")
    assert result1 == 5
    # Expected Output: 5

    # Test Case 2: No profit possible
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(prices2)
    print("Test Case 2:", result2, "Passed" if result2 == 0 else "Failed")
    assert result2 == 0
    # Expected Output: 0

    # Test Case 3: Single day prices
    prices3 = [5]
    result3 = solution.maxProfit(prices3)
    print("Test Case 3:", result3, "Passed" if result3 == 0 else "Failed")
    assert result3 == 0
    # Expected Output: 0

    # Test Case 4: Increasing prices
    prices4 = [1, 2, 3, 4, 5]
    result4 = solution.maxProfit(prices4)
    print("Test Case 4:", result4, "Passed" if result4 == 4 else "Failed")
    assert result4 == 4
    # Expected Output: 4

    # Test Case 5: Decreasing prices
    prices5 = [5, 4, 3, 2, 1]
    result5 = solution.maxProfit(prices5)
    print("Test Case 5:", result5, "Passed" if result5 == 0 else "Failed")
    assert result5 == 0
    # Expected Output: 0