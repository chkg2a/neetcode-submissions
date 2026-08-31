class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(subset[:])
                return 
            if i == len(nums):
                return
            if curr_sum > target:
                return
            for j in range(i,len(nums)):
                # if j > i and nums[j] == nums[j-1]:
                #     return
                subset.append(nums[j])
                backtrack(j , curr_sum + nums[j])
                subset.pop() 
        backtrack(0,0)
        return res