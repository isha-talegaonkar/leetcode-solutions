class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring = ''
        
        for char in s:
            if char in substring:
                cutIndex = substring.index(char)
                substring = substring[cutIndex+1:] + char
            else:
                substring += char
                result = max(result, len(substring))
        return result
                
        
#         chars = Counter()
#         left = right = 0
        
#         result = 0
        
#         while right < len(s):
#             r = s[right]
#             chars[r] += 1
            
#             while chars[r] > 1:
#                 l = chars[left]
#                 chars[l] -= 1
#                 left += 1
                
#             result = max(result, right - left + 1)
            
#             right += 1
        
#         return result

                
                    