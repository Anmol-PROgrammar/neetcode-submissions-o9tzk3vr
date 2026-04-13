class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # myMap = []
        res = 0
        if len(prices) < 2:
            return 0
        for i in range(0,len(prices) - 1):
            profit = max(prices[i+1:]) - prices[i]
            res = max (profit, res)
        return res
