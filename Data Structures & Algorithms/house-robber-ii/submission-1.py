class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        nums1 = nums[:n+1]
        nums2 = nums[1:]
        def dfs(i, arr):
            if i >= len(arr):
                return 0
            
            return max(arr[i] + dfs(i+2,arr),dfs(i+1,arr))
        left = dfs(0,nums1)
        right = dfs(0,nums2)
        return min(left,right)
