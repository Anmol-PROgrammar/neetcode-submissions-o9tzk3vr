class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i, j = 0, 1
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if (nums[i] == nums[j]): 
                    return True
                else:
                     j+=1
            i+=1; 
        return False;

                    