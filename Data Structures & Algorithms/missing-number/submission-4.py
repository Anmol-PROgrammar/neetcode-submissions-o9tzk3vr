class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0 
        expected = 0
        for i in range(0,n+1):
            expected += i
        for num in nums:
            sum += num
        return expected - sum
