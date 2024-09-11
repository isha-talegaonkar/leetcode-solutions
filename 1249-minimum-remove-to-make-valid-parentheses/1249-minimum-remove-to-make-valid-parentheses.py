class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indexes = set()
        
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes.add(i)
            else:
                stack.pop()
        indexes = indexes.union(set(stack))
        
        result = []
        
        for i, c in enumerate(s):
            if i not in indexes:
                result.append(c)
        return "".join(result)
        