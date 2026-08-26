class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums) 
        
        l = 0
        r = len(nums) - 1
        ans = 1

        while (l <= r):
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
                ans = l
            else:
                r = m - 1
        return l 