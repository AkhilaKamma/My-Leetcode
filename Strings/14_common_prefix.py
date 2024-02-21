class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Find the smallest string length
        minLen = len(strs[0])
        for each in strs:
            minLen = min(minLen,len(each))
        
        resPre = ""
        for i in range(minLen):
            currentChar = strs[0][i]
            for j in strs[1:]:
                if j[i] != currentChar:
                    return resPre
            resPre = resPre + currentChar
        return resPre
