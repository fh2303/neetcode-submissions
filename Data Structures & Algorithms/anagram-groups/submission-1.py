class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in hash:
                hash[key].append(strs[i])
            else:
                hash[key] = [strs[i]]
        return list(hash.values())
