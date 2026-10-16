class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charFreq = {}
        charFreq2 = {}
        chars = list(s)
        chars2 = list(t)
        for i in range(len(chars)):
            charFreq[chars[i]] = charFreq.get(chars[i], 0) + 1
        for i in range(len(chars2)):
            charFreq2[chars2[i]] = charFreq2.get(chars2[i], 0) + 1
        if charFreq == charFreq2:
            return True
        return False
