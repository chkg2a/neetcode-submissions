class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        subset = []
        def summation(i, current):
            if current == target:
                result.append(subset.copy())
                return
            
            if i >= len(nums) or current > target:
                return

            subset.append(nums[i])
            summation(i, nums[i] + current)
            subset.pop()
            summation(i + 1, current)
        summation(0,0)
        return result