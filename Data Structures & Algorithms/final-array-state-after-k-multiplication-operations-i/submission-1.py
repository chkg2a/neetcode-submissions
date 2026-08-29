class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            minN = float('inf')
            idx = -1
            for i in range(len(nums)):
                if nums[i] < minN:
                    minN = nums[i]
                    idx = i
            nums[idx] *= multiplier
            k -= 1
        return nums
        