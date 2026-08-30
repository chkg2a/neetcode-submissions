class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        last = nums[0]
        c_sum = nums[0]
        highest = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= last:
                last = nums[i]
                c_sum = nums[i]
            else:
                last = nums[i]
                c_sum += nums[i]
                highest = max(highest, c_sum)

        return highest