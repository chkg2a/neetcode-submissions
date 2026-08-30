class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current_path = []
        nums.sort()
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(current_path.copy())
                return 
            if curr_sum > target:
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                current_path.append(nums[j])
                backtrack(j, curr_sum + nums[j])
                current_path.pop()
        backtrack(0,0)
        return res