class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = []
        for i in candies:
            if (i+extraCandies) >= max(candies):
                temp.append(True)
            else:
                temp.append(False)
        return temp
                
        