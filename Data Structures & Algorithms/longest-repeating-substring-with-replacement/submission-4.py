class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = [0] * 26

        ans = 0
        i,j = 0,0 
        # while i < len(s):

        while j < len(s):
            hashMap[ord(s[j]) - ord("A")] += 1
            
            while (j-i+1) - max(hashMap) > k:
                hashMap[ord(s[i]) - ord("A")] -= 1
                i+=1
            ans = max(ans, j - i + 1)
            j+=1
                    
        # print(hashMap)
        return ans
