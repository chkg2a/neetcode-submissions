class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        writeIndex = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                nums[writeIndex] = nums[i]
                writeIndex += 1
        return writeIndex