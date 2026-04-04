class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map= {}
        for num in nums:
            map[num] = map.get(num,0)+1
        print(map)
        
        # freqList = [0] * (len(nums) + 1)
        freqList = [[] for i in range(len(nums) + 1)]
        for key,value in map.items():
            freqList[value].append(key)
        print (freqList)
        
        ans = []
        for m in range(len(freqList) - 1, 0, -1):
            for n in freqList[m]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return []