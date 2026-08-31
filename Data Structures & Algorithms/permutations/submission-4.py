class Solution :
    def permute(self,nums):
        self.res = []
        self.backtrack(nums,[],[False] * len(nums)) 
        return self.res

    def backtrack(self,nums,perm,pick):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(nums,perm,pick)
                perm.pop()
                pick[i] = False
