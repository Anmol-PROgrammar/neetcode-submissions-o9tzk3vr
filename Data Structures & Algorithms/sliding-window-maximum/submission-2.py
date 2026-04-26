class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(0, len(nums) - k + 1):
            max_in_window = max(nums[i : i + k])
            res.append(max_in_window)

        return res
