class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        ans = []
        for num in nums:
            myMap[num] =  myMap.get(num,0) + 1
        sortedMap = dict(sorted(myMap.items(), key=lambda item: item[1], reverse=True))
        # print(sortedMap)

        for i, (key, value) in enumerate(sortedMap.items()):
            if i == k:
                break
            ans.append(key)
        return ans