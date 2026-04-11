class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 pointers
        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                i+=1
            else:
                nums[k] = nums[i]
                k+=1

        return k