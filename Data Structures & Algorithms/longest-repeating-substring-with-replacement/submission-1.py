class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {i: 0 for i in range(26)}
        l = 0
        res = 0

        for r in range(len(s)):
            myMap[ord(s[r]) - ord('A')] += 1
            hFreq = max(myMap.values())

            while ((r - l + 1) - hFreq) > k:
                myMap[ord(s[l]) - ord('A')] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res