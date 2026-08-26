class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        subset = []
        def dfs(i,current):
            if current == target and subset not in result:
                result.append(subset.copy())
                return
            if i >= len(candidates) or current > target:
                return
            
            subset.append(candidates[i])
            dfs(i+1,current + candidates[i])

            subset.pop()
            while i + 1 < len(candiates) and candidates[i] == candidates[i+1]:
                i+= 1
            dfs(i+1,current)
        dfs(0,0)
        return result