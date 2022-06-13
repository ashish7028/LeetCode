class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[] for i in range(numRows)]
        
        for i in range(numRows):
            for j in range(i+1):
                if j < i:
                    if j == 0:
                        a[i].append(1)
                    else:
                        a[i].append(a[i-1][j] + a[i-1][j-1])
                elif i == j:
                    a[i].append(1)
        return a