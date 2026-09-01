class Solution:
    def climbStairs(self, n: int) -> int:
        i = 0
        j = 1
        for _ in range(n):
            temp = j
            j = j + i
            i = temp
        return j
