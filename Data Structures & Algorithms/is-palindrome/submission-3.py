class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        s = s.lower()
        start = 0 
        end = n - 1
        i = 0
        while start <= end:
            if not self.isAlphaNumeric(s[start]):
                start+=1
                continue
            if not self.isAlphaNumeric(s[end]):
                end-=1
                continue
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def isAlphaNumeric(self, s: str) -> bool:
        if (s >="a" and s<="z") or (s >="0" and s<="9"):
            return True
        return False

        