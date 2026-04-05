class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)

        s = s.lower()
        convertedString = ""
        for i in range(n):
            if (s[i] >="a" and s[i]<="z") or (s[i] >="0" and s[i]<="9"):
                convertedString+=s[i] 

        start = 0 
        end = len(convertedString) - 1

        while start <= end:
            if convertedString[start] != convertedString[end]:
                return False
            start += 1
            end -= 1
        return True


        