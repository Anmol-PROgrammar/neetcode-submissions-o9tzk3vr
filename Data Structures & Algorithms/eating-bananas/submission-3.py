class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        highestElement = max(piles)

        if h == n:
            return highestElement

        k = highestElement

        l = 1
        r = highestElement

        while l <= r:
            mid = l + (r - l) // 2
            pileToFinish = 0
            for i in range(0, n):
                pileToFinish += math.ceil(piles[i]/mid)
            if pileToFinish <= h:
                k = min(k,mid)
                r = mid - 1
            else:
                l = mid + 1

        return k
        