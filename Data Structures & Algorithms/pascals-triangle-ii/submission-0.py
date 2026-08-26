class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [1] * (rowIndex + 1) 

        for i in range(2,rowIndex + 1):
            for j in range(1, i):
                rows[i - j] += rows[i -j - 1]
        return rows