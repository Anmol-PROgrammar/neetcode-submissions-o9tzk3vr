class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        current = 0
        i = 0 
        j = n -  1
        while i < j :
            current  = min(heights[i],heights[j]) *  (j - i)
            res = max(res,current)
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] > heights[j]:
                j-=1
            else:
                i+=1
            
        return res