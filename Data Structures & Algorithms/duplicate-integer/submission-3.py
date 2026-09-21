class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        xor = set()
        for i in nums:
            if i not in xor:
                xor.add(i) 
            else:
                return True
        return False