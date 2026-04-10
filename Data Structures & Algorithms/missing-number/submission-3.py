class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n+1):
            flag = False
            for j in range(0,n):
                if nums[j] == i:
                    flag = True
                    # n-=1
                    break
            if flag == False:
                return i