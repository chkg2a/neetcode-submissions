class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []
        def backtrack(i,curr_sum):
            if curr_sum == target:
                res.append(subset[:])
                return
            if curr_sum > target or len(candidates)  == i:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] ==candidates[j -1]:
                    continue
                subset.append(candidates[j])
                backtrack(j+1,curr_sum + candidates[j])
                subset.pop()
        backtrack(0,0)
        return res