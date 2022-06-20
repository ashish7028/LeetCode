class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        size = len(s)
        shuffle_s = [' ' for _ in range(size)]
        
        for idx, char in enumerate(s):
            shuffle_s[ indices[idx] ] = char
            
        return ''.join(shuffle_s)