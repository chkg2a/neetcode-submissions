class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hi = max(nums)
        res = []
        for i in range(1,hi):
            if i not in nums:
                res.append(i)
        return res