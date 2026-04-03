class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        myMap = {}
        for i,num in enumerate(nums):
            diff =  target - num;
            if myMap.get(diff) != None:
                return [myMap[diff],i]
            else: 
                myMap[num] = i;
        return [];   
