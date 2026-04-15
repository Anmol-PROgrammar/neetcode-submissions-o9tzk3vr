class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m, n = len(s1), len(s2)
        if m > n:
            return False

        myMap = {}
        for ch in s1:
            myMap[ch] = myMap.get(ch, 0) + 1

        i = 0
        count = m  # total chars we need to match

        for j in range(n):
            # If char is useful
            if s2[j] in myMap:
                if myMap[s2[j]] > 0:
                    count -= 1
                myMap[s2[j]] -= 1

            # When window size exceeds m, shrink from left
            if j - i + 1 > m:
                if s2[i] in myMap:
                    if myMap[s2[i]] >= 0:
                        count += 1
                    myMap[s2[i]] += 1
                i += 1

            # Check if valid permutation found
            if count == 0:
                return True

        return False