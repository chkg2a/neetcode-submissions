class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        visited = set()
        def dfs(index):
            if index >= len(nums) - 1:
                return True
            
            if index in visited:
                return False

            visited.add(index)
            for jump in range(1,nums[index] + 1):
                if (dfs(index + jump)):
                    return True

            return False
        
        return dfs(0)
