class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * (len(nums) + 2)
        n = len(nums)
        nums1 = nums[:n-1]
        nums2 = nums[1:]
        def dfs(i, arr):
            if dp[i] != 0:
                return dp[i]
            if i >= len(arr):
                return 0

            dp[i] = max(arr[i] + dfs(i+2,arr),dfs(i+1,arr))
            
            return dp[i]
        left = dfs(0,nums1)
        right = dfs(0,nums2)
        return max(left,right)
