class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = set()
        for i in nums:
            mySet.add(i)
        unique = sorted(mySet)
        for i,n in enumerate(unique):
            nums[i] = n

        return len(mySet)
