class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str in strs:
            size = len(str)
            encoded = encoded + f"{size}#" + str
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded =[]
        strLength = ""
        i = 0 
        while i < len(s):
            if s[i]>='0' and s[i]<='9':
                strLength+=(s[i])
            if s[i] == '#' and len(strLength) != 0:
                decoded.append(s[i + 1: i + int(strLength) + 1])
                i += int(strLength)
                strLength = ""
            i+=1
        return decoded