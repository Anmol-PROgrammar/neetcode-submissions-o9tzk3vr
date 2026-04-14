class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n = len(piles)
        highestElement = max(piles)  # max possible eating speed (eat largest pile in 1 hour)

        # if hours allowed == number of piles, koko must eat each pile in exactly 1 hour
        # so minimum speed = largest pile
        if h == n:
            return highestElement

        k = highestElement  # stores our answer, initialized to worst case (max speed)

        # answer has to lie between 1 (minimum 1 banana/hr) and max pile (worst case speed)
        # we could check every speed 1,2,3...max but that's O(max) per check
        # instead binary search this range to find minimum valid k in O(log max) jumps
        l = 1
        r = highestElement

        while l <= r:
            mid = l + (r - l) // 2  # candidate speed to test (avoids overflow)

            # calculate total hours needed to finish all piles at speed = mid
            pileToFinish = 0
            for i in range(0, n):
                pileToFinish += math.ceil(piles[i] / mid)  # hours for each pile = ceil(pile/speed)

            if pileToFinish <= h:
                # mid speed is feasible, try slower (search left for minimum)
                k = min(k, mid)  # update answer
                r = mid - 1
            else:
                # mid speed too slow, need faster speed (search right)
                l = mid + 1

        return k  # minimum feasible eating speed