class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        n = len(nums)
        if n <= 1:
            return nums[0]

        current = nums[0]
        i = 1
        while i < n:
            if current < 0:
                current = nums[i]
            else:
                current += nums[i]
            maxsum = max(maxsum, current)
            i += 1

        return maxsum