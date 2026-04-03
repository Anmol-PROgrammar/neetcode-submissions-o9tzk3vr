class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        myMapS, myMapT = {},{};
        for i in range(len(s)):
            myMapS[s[i]] = 1 + myMapS.get(s[i],0)
            myMapT[t[i]] = 1 + myMapT.get(t[i],0)

        return myMapS == myMapT
        