class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        longest = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue                    # skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                curr += 1                  # extend sequence
            else:
                longest = max(longest, curr)
                curr = 1                   # reset sequence

        return max(longest, curr)
