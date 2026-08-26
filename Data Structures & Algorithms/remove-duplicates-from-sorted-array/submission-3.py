class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_len = len(nums)
        new_set = set(nums)
        for i in range(1,curr_len):
            if i + 1 > curr_len:
                break
            if nums[i - 1] == nums[i]:
                print(nums[i])
                nums.remove(nums[i])
                curr_len -=1
            
        return len(new_set)