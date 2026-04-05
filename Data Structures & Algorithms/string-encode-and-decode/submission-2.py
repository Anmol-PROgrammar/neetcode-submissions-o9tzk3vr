class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            size = len(str)
            encoded = encoded + f"{size}#" + str
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded =[]
        i,j = 0,0
        while i < len(s):
            if s[j] != "#":
                j+=1
            else: 
                sub = s[i:j]
                decoded.append(s[j+1:j+int(sub)+1])
                i = j + int(sub) + 1
                j = i
        return decoded