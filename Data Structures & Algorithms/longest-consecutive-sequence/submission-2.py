class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        max_seq = 0
        long_seq = 1
        for i in range(1,len(nums)):
            if nums[i] == 1 + nums[i-1]:
                long_seq += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                long_seq = 1
            max_seq = max(max_seq,long_seq)
        return max_seq