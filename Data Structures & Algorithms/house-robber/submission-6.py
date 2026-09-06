class Solution:
    def rob(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for i in range(len(nums)):
            nums[i] = max(nums[i] + x,y)
            x,y = y, nums[i]
        return y