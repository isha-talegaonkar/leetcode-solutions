class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        chars = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }
        result = []
        
        def backtrack(index, combination):
            if len(combination) == len(digits):
                result.append(combination)
                return
            
            for char in chars[digits[index]]:
                backtrack(index+1, combination+char)
        
        backtrack(0, "")
        
        return result