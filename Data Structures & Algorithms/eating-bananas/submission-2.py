class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        highestElement = max(piles)

        if h == n:
            return highestElement
        # print (math.ceil(1000000000/375000000))
        currK = highestElement
        k = highestElement

        l = 1
        r = highestElement

        while l <= r:
            mid = l + (r - l) // 2
            pileToFinish = 0
            for i in range(0, n):
                print(f" ceil value=  {math.ceil(piles[i]/mid)}, prev pile = {pileToFinish}")
                pileToFinish += math.ceil(piles[i]/mid)
            print(f"pileToFinish: {pileToFinish}, mid: {mid}, min k: {k}")
            if pileToFinish <= h:
                k = min(k,mid)
                r = mid - 1
                print(f"Valid K: {k}")
            else:
                l = mid + 1
                print(f"InValid K: {k}")
                # return k

        return k
        