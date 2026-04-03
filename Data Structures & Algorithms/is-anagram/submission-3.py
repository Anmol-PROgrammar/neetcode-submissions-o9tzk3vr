class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        myMap = {};

        for i in s:
            if  i in myMap:
                myMap[i] += 1
            else: 
                myMap[i] = 1

        for j in t:
            if j in myMap:
                myMap[j] -= 1
            else: 
                return False
        
        for k in myMap:
            if myMap[k] != 0:
                return False
        return True
        