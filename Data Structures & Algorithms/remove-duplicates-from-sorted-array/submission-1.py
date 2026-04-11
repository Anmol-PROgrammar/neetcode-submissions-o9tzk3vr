class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != unique[-1]:
                unique.append(nums[i])
                i+=1
        k =  len(unique)
        for i in range(0,k):
            nums[i] = unique[i] 
        return k
