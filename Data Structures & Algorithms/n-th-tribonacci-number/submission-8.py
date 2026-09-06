class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        t0 = 0
        t1 = 1
        t2 = 1
        for _ in range(2,n):
            temp = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = temp
        return t2
