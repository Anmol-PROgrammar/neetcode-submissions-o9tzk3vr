class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force, time O(n^3) and space O(n^2)
        # s = set()
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             #print(i,j,k)
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 s.add(tuple(sorted([nums[i], nums[j], nums[k]])))


        # return [list(v) for v in s]

        # optimising for time O(n^2) and space

        # res = []
        # nums.sort() # nlogn in place

        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i - 1]: # skip repeating a values.
        #         continue

        #     # continue with 2 sum problem

        #     l, r = i + 1, len(nums) - 1

        #     while l < r:
        #         ts = a + nums[l] + nums[r]
        #         if ts > 0:
        #             r -= 1
        #         elif ts < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l +=1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1

        # return res

        # alternative 

        res = set()
        n, p, z = [], [], []
        for v in nums:
            if v < 0:
                n.append(v)
            elif v > 0:
                p.append(v)
            else:
                z.append(v)

        N, P = set(n), set(p)

        if len(z)>2:
            res.add((0,0,0))

        if len(z) > 0:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        for i in range(0, len(n)):
            for j in range(i + 1, len(n)):
                t = -(n[i] + n[j])
                if t in P:
                    res.add(tuple(sorted([n[i],n[j], t])))

        for i in range(0, len(p)):
            for j in range(i + 1, len(p)):
                t = -(p[i] + p[j])
                if t in N:
                    res.add(tuple(sorted([p[i], p[j], t])))

        return list(res)
        

                        

        