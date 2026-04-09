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
            j = i + 1
            best = i + 1
            stones = 0
            stones_at_best = 0

            while j < n:
                if height[j] >= height[i]:       # ideal wall, calculate and move i
                    res += height[i] * (j - i - 1) - stones
                    i = j
                    break
                if height[j] > height[best]:     # new best right wall
                    best = j
                    stones_at_best = stones          # stones strictly between i and best
                stones += height[j]
                j += 1
            else:                                    # no ideal wall found, settle for best
                res += height[best] * (best - i - 1) - stones_at_best
                i = best

        return res