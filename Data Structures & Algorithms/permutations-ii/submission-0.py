class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        cnt = Counter(nums)
        
        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for num in cnt:
                if cnt[num] > 0:
                    subset.append(num)
                    cnt[num] -= 1
                    backtrack()
                    cnt[num] += 1
                    subset.pop()
        backtrack()
        return res