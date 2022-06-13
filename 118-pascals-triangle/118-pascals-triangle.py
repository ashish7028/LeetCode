class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j==i :
                    temp.append(1)
                else:
                    temp.append(result[i-1][j-1] +result[i-1][j] )
            result.append(temp)
        return result
		
        
"""class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp,row = [[1]],1
        while row < numRows:
            temp.append([1])
            for i in range(1,row):
                temp[row].append(temp[row-1][i-1] + temp[row-1][i])
            temp[row].append(1)
            row += 1
        return temp
		"""        