class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        
        for jwel in J:
            count += S.count(jwel)
        
        return count