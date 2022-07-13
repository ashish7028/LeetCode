class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        a = s.split()[:k]
        
        return ' '.join(a)
            
            
            
        