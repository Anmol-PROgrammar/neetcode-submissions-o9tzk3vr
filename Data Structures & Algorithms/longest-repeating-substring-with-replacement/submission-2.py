class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {i:0  for i in range(26)}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            # insert element 
            myMap[ord(s[r]) - ord('A')] += 1
            # find max freq in the window
            hFreq = max(myMap.values())

            # check if current window size - highest ferq <= k(replacement allowed) 
            # if yes increase window to right 
            # if no decrease window from left untill logic is valid again 
            if ((r - l + 1) - hFreq) <= k:
                print ("adding:: ",res, r - l +1 , l , r, "high feq = ",hFreq)
                res = max(res,r-l+1)
            else:
                print ("removing",res, r - l +1 , l , r, "high feq = ",hFreq)
                # remove left element from dict
                myMap[ord(s[l]) - ord('A')] -= 1
                l+=1
            r+=1

        # print(myMap)
        return res