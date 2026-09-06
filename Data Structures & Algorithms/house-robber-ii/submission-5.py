class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * (len(nums) + 2)
        dp2 = [0] * (len(nums) + 2)
        for i in range(2,len(nums) + 1):
            dp1[i] = max(nums[i - 2] + dp1[i - 2], dp1[i - 1])
        for i in range(3,len(nums) + 2):
            dp2[i] = max(nums[i - 2] + dp2[i - 2], dp2[i - 1])
        maxL = 0
        print(dp1)
        print(dp2)
        for i in range(len(dp1)):
            maxL = max(maxL,dp1[i], dp2[i])
        return maxL