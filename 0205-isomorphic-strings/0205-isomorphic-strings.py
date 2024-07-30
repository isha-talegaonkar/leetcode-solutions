class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                else:
                    hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return True