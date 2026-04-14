class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        maxCount = 0
        counter = 0 
        mySet = set()
        while j < len(s):
            if not s[j] in mySet:
                counter = j - i + 1
                maxCount = max(maxCount, counter)
                mySet.add(s[j])
                j+=1
            else:
                while i < j:
                    print (i , j)
                    if s[i] == s[j]:
                        mySet.remove(s[i])
                        i+=1                        
                        break
                    else:
                        mySet.remove(s[i])
                        i+=1                        
            
        return maxCount
