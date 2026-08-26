class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hi = max(nums)
        res = []
        for i in range(1,hi + 1):
            if i not in nums:
                res.append(i)
        if len(res) == 0:
            res.append(hi + 1)
        return res