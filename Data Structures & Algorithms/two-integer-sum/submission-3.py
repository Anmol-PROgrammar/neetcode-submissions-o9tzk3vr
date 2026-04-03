class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans = []
        i = 0
        myMap = {}
        for i,num in enumerate(nums):
            myMap[num] = i;

        for i,num in enumerate(nums):
            diff =  target - num;
            if myMap.get(diff) and i != myMap[diff]:
                return [i,myMap[diff]]

        return ans;   
