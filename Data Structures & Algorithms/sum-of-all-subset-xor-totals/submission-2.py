class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        subset = []
        def backtrack(i):
            res.append(subset.copy())
            if i == len(nums):
                return 
            for j in range(i,len(nums)):
                subset.append(nums[j])
                backtrack(j+1)
                subset.pop()
        sum = 0
        backtrack(0) 
        for s in res:
            xor = 0
            for x in s:
                xor ^= x
            sum+=xor
        return sum