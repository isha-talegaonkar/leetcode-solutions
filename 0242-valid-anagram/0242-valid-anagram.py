class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        
        counter = defaultdict(int)
        for i in s:
            counter[i] +=1
        
        for j in t:
            counter[j] -=1
        
        for value in counter.values():
            if value != 0:
                return False
        
        return True
        
        # return collections.Counter(s) == collections.Counter(t)