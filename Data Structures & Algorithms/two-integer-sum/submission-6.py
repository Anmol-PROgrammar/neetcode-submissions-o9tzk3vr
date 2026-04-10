class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            sum = 0
            myMap = []

            for i,n in enumerate(nums):
                myMap.append([n,i])

            # print(myMap)     
            myMap.sort()
            i = 0
            j = len(nums) -1 
            while i < j:
                sum = myMap[i][0] + myMap[j][0]
                if target < sum:
                    j-=1
                elif target > sum:
                    i+=1
                else:
                    return [min(myMap[i][1],myMap[j][1]),max(myMap[i][1],myMap[j][1])]
            return []
        