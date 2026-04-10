class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        current = nums[0]
        i = 1
        n = len(nums)
        while i < n:
            if nums[i] > current and current < 0:
                current = nums[i]        # start new window
            else:
                current += nums[i]       # extend window
            
            maxsum = max(maxsum, current)
            i += 1

        return maxsum