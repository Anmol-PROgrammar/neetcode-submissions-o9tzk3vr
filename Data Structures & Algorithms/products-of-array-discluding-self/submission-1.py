class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        pref= [0] * n
        suff= [0] * n


        pref[0] = suff[n - 1] = 1
        # create prefix array
        for i in range(1, n):
            # print(pref[i],pref[i-1],nums[i-1])
            pref[i] = pref[i - 1] * nums[i - 1]

        # create suffix array
        for i in range(n - 2,-1,-1):
            # print(suff[i],suff[i+1],nums[i+1])
            suff[i] = suff[i + 1] * nums[i + 1]

        for i in range(n):
            output[i] = pref[i] * suff[i]

        return output