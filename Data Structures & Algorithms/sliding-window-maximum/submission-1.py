class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i= 0
        res = [];
        

        while i <= len(nums) - k:
            j = i
            curr_max = -math.inf;
            while j < i + k:
                curr_max = max(curr_max,nums[j]);
                j+=1;
            res.append(curr_max);
            i+=1;

        return res