class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = [[]]
        res = 0
        for num in nums:
            new_subsets = [curr + [num] for curr in subsets]
            subsets.extend(new_subsets)
        
        for l in subsets:
            val = 0
            for item in l:
                val ^= item
            res += val
        return res