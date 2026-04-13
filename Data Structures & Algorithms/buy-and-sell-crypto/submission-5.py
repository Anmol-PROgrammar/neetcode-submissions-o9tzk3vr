class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        res = 0
        while i < len(prices) - 1:
            # print(prices[i],prices[j])
            if j == len(prices):
                break
            elif prices[i] > prices[j]:
                i = j
            else: 
                res = max(prices[j]- prices[i], res)
            j+=1
        return res
