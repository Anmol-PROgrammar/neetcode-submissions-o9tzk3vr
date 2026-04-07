class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        nums.sort()
        if nums[-1] < 0:
            return []
        if nums[0] > 0:
            return []
        res = []

        for i, val in enumerate(nums[:-2]):
            if (val > 0):
                break
            if i> 0 and nums[i-1] == val:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum > -val:
                    r -= 1
                elif twoSum < -val:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res
       