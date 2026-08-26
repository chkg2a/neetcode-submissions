class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num =  math.prod(nums)
        if num > 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1
