memo = [-1] * 38
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        if memo[n] != -1:
            return memo[n] 
        memo[n] =  self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n - 3)
        return memo[n]