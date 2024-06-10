class Solution:
    def longestPalindrome(self, s: str) -> int:
        characters = set()
        res = 0
        
        for char in s:
            if char in characters:
                characters.remove(char)
                res += 2
            else:
                characters.add(char)
        
        if characters:
            res += 1
        
        return res