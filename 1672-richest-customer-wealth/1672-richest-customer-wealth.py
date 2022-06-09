class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp = []
        
        for i in accounts:
            t = 0
            t = sum(i)
            temp.append(t)
        return max(temp)
    
            