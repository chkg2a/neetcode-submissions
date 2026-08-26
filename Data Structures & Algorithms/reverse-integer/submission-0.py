class Solution:
    def reverse(self, x: int) -> int:
        MAX = (1 << 31) - 1
        MIN = -(1 << 31)

        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x / 10)

            if ((MAX / 10 < res) or
                (MAX / 10 == res and MAX % 10 >= digit)):
                return 0
            if ((MIN / 10 > res) or
                (MIN / 10 == res and MIN % 10 <= digit)):
                return 0
            res = res * 10 + digit

        return res
