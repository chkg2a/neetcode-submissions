class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        first = 1
        second = 1
        finalSum = first + second
        for i in range(2,n):
            first = second
            second = finalSum
            finalSum = first + second
            print(finalSum)
        return finalSum