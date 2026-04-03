class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set();
        for i in nums:
            if i in mySet:
                return True
            else:
                mySet.add(i)
        return False
                    