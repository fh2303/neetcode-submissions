class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        aGroup = {}
        for i in range(len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            if sortedStr in aGroup:
                aGroup[sortedStr].append(strs[i])
            else:
                aGroup[sortedStr]=[strs[i]]
        return list(aGroup.values())
                

