class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) % 2 == 0:
            even = True
        else:
            even = False
        sum = 0
        if even:
            for i in range(len(mat)):
                sum += mat[i][i]
            for i in range(len(mat) - 1,-1,-1):
                sum += mat[abs(i - len(mat)) - 1][i]

        else:
            for i in range(len(mat)):
                sum += mat[i][i]
            for i in range(len(mat) - 1,-1,-1):
                sum += mat[abs(i - len(mat)) - 1][i]
            sum -= mat[len(mat) // 2][len(mat) // 2]
        return sum

            
