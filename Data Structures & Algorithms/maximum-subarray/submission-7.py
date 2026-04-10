class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        res = -math.inf
        if n == 1:
            return  nums[0]

        while i < n:
            curr = 0
            maxSum = -math.inf
            j = i
            while j < n:
                curr +=nums[j]
                j+=1
                res = max(curr, res)
            i+=1

        return res

