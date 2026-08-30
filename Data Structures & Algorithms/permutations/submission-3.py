class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums,[], [False]* len(nums))
        return self.res
    def backtrack(self, nums: List[int], perm: List[int], pick: List[bool]):
        if len(nums) == len(perm):
            self.res.append(perm[:])
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(nums,perm,pick)
                perm.pop()
                pick[i] = False