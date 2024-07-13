class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : len(word)+i] == word:
                        dp[i] = dp[len(word)+i]
                if dp[i]:
                    break
        
        return dp[0]