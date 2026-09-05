class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        writeIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[writeIndex] = nums[i]
                writeIndex += 1
        for i in range(len(nums)-1,writeIndex - 1,-1):
            nums[i] = 0