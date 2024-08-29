class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def helper(bracket, left, right):
            if len(bracket) == 2*n:
                result.append(bracket)
            
            if left > 0:
                helper(bracket + '(', left - 1, right)
            
            if right > 0 and right > left:
                helper(bracket + ')', left, right-1)
        
        helper("", n, n)
        
        return result