class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        if k == len(nums):
            return nums

        count = Counter(nums)
            # output eg: {1:3,2:2,3:1}
        return heapq.nlargest(k, count.keys(), key=count.get)
            # k is the target number we are looking for
            # count.keys() this is the data source, they key of the values
            # key = count.get this is tell the rules. need to compare frequency not the numbrt itself
        return topk(nums, k) #返回k个数