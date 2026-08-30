class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_path = []
        def backtrack(i):
            res.append(current_path.copy())
            if i >= len(nums):
                return
            for j in range(i,len(nums)):
                current_path.append(nums[j])
                backtrack(j+1)
                current_path.pop()
        backtrack(0)
        return res