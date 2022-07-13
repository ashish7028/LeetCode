class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        temp = []
        a = s.split()[:k]
        
        return ' '.join(a)
            
            
            
        