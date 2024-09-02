class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.dfs(s, [], result)
        
        return result
    
    def isPalindrome(self, s):
        return s == s[::-1]
    def dfs(self, s, path, result):
        if not s:
            result.append(path)
            return
        
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], result)
        