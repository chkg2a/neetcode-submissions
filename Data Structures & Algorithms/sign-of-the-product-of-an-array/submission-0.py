class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n_count = 0
        for i in nums:
            if i < 0:
                n_count += 1
            if i == 0:
                return 0
        if n_count % 2 == 1:
           return -1 
        elif n_count % 2 == 0:
            return 1
        else:
            return 0