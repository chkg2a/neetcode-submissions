class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        def helper(rowIndex):
            rows = [0] *(rowIndex + 1)
            rows[0] = 1

            for i in range(1,rowIndex + 1):
                for j in range(i, 0, -1):
                    rows[j] += rows[j - 1]
            return rows

        for i in range(numRows):
            res.append(helper(i))
        return res