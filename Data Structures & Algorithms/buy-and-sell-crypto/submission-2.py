class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        myMap = []
        if len(prices) <= 1:
            return 0
        for i in range(0,len(prices) - 1):
            profit = max(prices[i+1:]) - prices[i]
            myMap.append(profit)
        print(myMap)
        return max(max(myMap),0)
