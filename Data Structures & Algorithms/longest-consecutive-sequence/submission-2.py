class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        nums.sort()
        print (nums)
        currSeq,longSeq = 1,0

        i = 0 
        while i < n - 1:
            j = i+1
            if nums[j] == nums[i]:
                i+=1
                continue
            elif nums[j] == nums[i] + 1:
                currSeq += 1
            elif nums[j] != nums[i] + 1:
                if longSeq < currSeq:
                    longSeq = currSeq
                currSeq = 1
            i += 1
        if longSeq < currSeq:
            longSeq = currSeq
        return longSeq










