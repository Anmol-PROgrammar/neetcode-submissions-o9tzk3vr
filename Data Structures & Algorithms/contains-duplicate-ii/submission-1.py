class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        myMap = []

        for i,n in enumerate(nums):
            myMap.append([n,i])
        myMap.sort()
        # print(myMap)
        i = 0
        while i < len(myMap) - 1:
            j = i+1
            print(i,j)
            if myMap[i][0] == myMap[j][0] and myMap[j][1] - myMap[i][1] <=k:
                return True
            i+=1

        return False