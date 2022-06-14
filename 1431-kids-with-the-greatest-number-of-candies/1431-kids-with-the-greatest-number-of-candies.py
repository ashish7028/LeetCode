class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = []
        for i in candies:
            temp.append((i+extraCandies) >= max(candies))
        return temp
                
     