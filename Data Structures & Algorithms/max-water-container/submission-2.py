class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        current = 0
        for i in range(0, n):
            for j in range(i+1, n):
                current = min(heights[i],heights[j]) *  (j - i)
                res = max(res,current) 
                j += 1
            i += 1
        return res
                