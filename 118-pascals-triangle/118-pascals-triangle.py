class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        temp,row = [[1]],1
        while row < numRows:
            temp.append([1])
            for i in range(1,row):
                temp[row].append(temp[row-1][i-1] + temp[row-1][i])
            temp[row].append(1)
            row += 1
        return temp
		