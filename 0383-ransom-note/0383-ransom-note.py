class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        magazine_counts = {}
        for m in magazine:
                magazine_counts[m] = magazine_counts.get(m, 0) + 1
        
        ransomNote_counts = {}
        for r in ransomNote:
            ransomNote_counts[r] = ransomNote_counts.get(r, 0) + 1
        
        for char, count in ransomNote_counts.items():
            magazine_count = magazine_counts.get(char, 0)
            if  magazine_count < count:
                return False
        
        return True
