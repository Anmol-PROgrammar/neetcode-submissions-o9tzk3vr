class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        maxCount = 0
        counter = 0 
        mySet = set()
        print(s)
        while j < len(s):
            if not s[j] in mySet:
                counter = j - i + 1
                maxCount = max(maxCount, counter)
                mySet.add(s[j])
                print(f"adding in set {mySet}")
                j+=1
            else:
                while i < j:
                    print (i , j)
                    print(f"before remove {mySet}")
                    if s[i] == s[j]:
                        mySet.remove(s[i])
                        # counter = j - i + 1
                        i+=1                        
                        break
                    else:
                        mySet.remove(s[i])
                        i+=1                        
                    print(f"after remove {mySet}")
            
        return maxCount
