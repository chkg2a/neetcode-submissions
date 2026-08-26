class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        even = True
        for i in nums:
            if i % 2 == 0 and even == False:
                return False
            elif i % 2 == 1 and even == True:
                return False
            if i % 2 == 0 and even == True:
                even = False
            elif i % 2 == 1 and even == False:
                even = True
            
        return True