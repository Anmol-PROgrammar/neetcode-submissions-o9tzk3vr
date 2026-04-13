class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0 ,len(prices) - 1):
            currProfit = 0
            for j in range(i+1,len(prices)):
                currProfit =  prices[j] - prices[i]
                # print(f"DayToBuy= {prices[i]}, DayToSell= {prices[j]}")
                maxProfit = max(maxProfit, currProfit)
                # print(f"maxProfit= {maxProfit}, currProfit= {currProfit}")
        return maxProfit
                
