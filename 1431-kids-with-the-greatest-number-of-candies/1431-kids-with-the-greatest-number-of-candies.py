class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = []
        for i in candies:
            temp.append((i+extraCandies) >= max(candies))
        return temp
                
        """class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = []
        for i in candies:
            if (i+extraCandies) >= max(candies):
                temp.append(True)
            else:
                temp.append(False)
        return temp"""