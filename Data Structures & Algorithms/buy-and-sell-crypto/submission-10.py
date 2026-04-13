class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        best = 0
        min_sf = prices[0]

        for i in range(1, n):
            if prices[i] < min_sf:
                min_sf = prices[i]
            if prices[i] - min_sf > best:
                best = prices[i] - min_sf

        return best