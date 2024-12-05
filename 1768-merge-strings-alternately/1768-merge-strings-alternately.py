class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        word1Len = len(word1)
        word2Len = len(word2)
        
        i=0
        j=0
        
        while i< word1Len or j<word2Len:
            if i < word1Len:
                result += word1[i]
                i += 1
            if j < word2Len:
                result += word2[j]
                j += 1
            
        
        return "".join(result)