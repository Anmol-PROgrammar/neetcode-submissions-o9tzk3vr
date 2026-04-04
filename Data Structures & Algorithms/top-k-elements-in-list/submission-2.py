class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
        
        freqList = []
        for key,value in map.items():
            freqList.append([value,key])
        
        freqList.sort(reverse=True)

        ans = []
        for i in range(len(freqList)):
            if i < k:
                ans.append(freqList[i][1])
        return ans