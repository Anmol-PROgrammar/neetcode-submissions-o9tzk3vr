class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        res = 0

        while i < n - 1:
            # skip ascending slope, not a valid left wall
            if height[i] < height[i + 1]:
                i += 1
                continue

            # find best right wall
            right = i + 1
            best = i + 1
            stones = 0
            stones_at_best = 0

            while right < n:
                if height[right] >= height[i]:       # ideal wall, calculate and move i
                    res += height[i] * (right - i - 1) - stones
                    i = right
                    break
                if height[right] > height[best]:     # new best right wall
                    best = right
                    stones_at_best = stones          # stones strictly between i and best
                stones += height[right]
                right += 1
            else:                                    # no ideal wall found, settle for best
                res += min(height[i], height[best]) * (best - i - 1) - stones_at_best
                i = best

        return res