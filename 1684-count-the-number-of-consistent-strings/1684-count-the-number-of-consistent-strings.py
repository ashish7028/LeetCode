class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:    
        A = set(allowed)
        n = 0
        for x in words:
            if set(x).issubset(A):
                n += 1
        return n
        
        