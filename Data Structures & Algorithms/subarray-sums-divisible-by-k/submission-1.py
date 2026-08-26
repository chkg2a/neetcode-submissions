class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] = nums[i - 1] + nums[i]
         
        count = -1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] % k == 0:
                    count += 1
        return count