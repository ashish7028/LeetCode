class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        temp = 0
        for i in operations:
            if (i == "++X" or i =="X++"):
                temp += 1
            else:
                temp -= 1
        return temp
        