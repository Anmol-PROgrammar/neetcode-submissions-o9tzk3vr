class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m, n = len(s1), len(s2)

        i = 0
        j = m

        if m > n:
            return False

        s1_sorted = sorted(s1)
        while j <= n:
            if sorted(s2[i:j]) == s1_sorted:
                return True
            else:
                i += 1
                j += 1

        return False