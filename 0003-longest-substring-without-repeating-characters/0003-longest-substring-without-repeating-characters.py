class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        substring = ''
        
        for char in s:
            if char not in substring:
                substring += char
                ans = max(ans, len(substring))
            else:
                cut = substring.index(char)
                substring = substring[cut+1:] + char
        return ans
                
                    