class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashSet = set()
        highest = 1
        for i in nums:
            if i < 0:
                continue
            highest = max(highest,i)
            hashSet.add(i)
        for i in range(1,highest+1):
            if i in hashSet:
                continue
            return i
        return highest + 1