class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s:
                return [i-1,i]