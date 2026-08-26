class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subArr = []
        for i in range(len(nums)):
            current = []
            for j in range(i, len(nums)):
                current = current + [nums[j]]
                subArr.append(current)
        
        count = 0
        for arr in subArr:
            if sum(arr) % k == 0:
                count += 1
        return count