class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        i = 0;
        while i < len(strs):
            j = i + 1;
            currentGroup = [strs[i]]
            while j < len(strs):
                if sorted(strs[i]) == sorted(strs[j]):
                    currentGroup.append(strs[j]);
                    strs.pop(j)
                    j-=1;
                j+=1;
            i+=1
            output.append(currentGroup);
        return output