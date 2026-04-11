class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0 , len(nums) - 1
        # index_to_insert = -1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r =  mid
            else:
                l = mid + 1

        if nums[l] < target:
            return l+1
        return l