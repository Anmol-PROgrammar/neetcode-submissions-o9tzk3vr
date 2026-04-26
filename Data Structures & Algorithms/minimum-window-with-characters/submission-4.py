
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
            while counter == 0:  # window is valid, try to shrink

                window = s[i:j]  # current window string

                # save if first window found, or smaller than previous best
                if min_sub == "" or len(window) < len(min_sub):
                    min_sub = window

                # s[i] is being removed from window
                # only care if it belongs to t
                if s[i] in myMap:
                    myMap[s[i]] += 1          # give back its count
                    if myMap[s[i]] > 0:       # if count goes above 0, window is now invalid
                        counter += 1          # counter != 0, while loop will stop

                i += 1  # shrink from left

        return min_sub
