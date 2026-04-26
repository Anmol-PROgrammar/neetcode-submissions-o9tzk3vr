
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)

        if m < n:
            return ""

        origMap = {}
        for c in t:
            origMap[c] = origMap.get(c, 0) + 1

        myMap = origMap.copy()
        counter = n
        i, j = 0, 0
        min_sub = ""

        while j < m:
            # expand right
            if s[j] in myMap:
                if myMap[s[j]] > 0:
                    counter -= 1
                myMap[s[j]] -= 1
            j += 1

            # shrink left when valid window found
            while counter == 0:
                window = s[i:j]
                if not min_sub or len(window) < len(min_sub):
                    min_sub = window
                if s[i] in myMap:
                    myMap[s[i]] += 1
                    if myMap[s[i]] > 0:
                        counter += 1
                i += 1

        return min_sub
