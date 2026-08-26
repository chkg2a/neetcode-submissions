class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        maxArea = 0
        while i < j:
            maxArea = max(maxArea,abs(i - j)*min(nums[i],nums[j]))
            if nums[i] <= nums[j]:
                i += 1
            else:
                j -= 1

        return maxArea