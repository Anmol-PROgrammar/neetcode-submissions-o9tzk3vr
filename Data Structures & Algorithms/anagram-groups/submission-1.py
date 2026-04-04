class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for str in strs:
            sortedStr = "".join(sorted(str))
            myDict[sortedStr].append(str)
        return list(myDict.values())