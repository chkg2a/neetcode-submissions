class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        curr_path = []
        
        # CRITICAL: Must sort to handle duplicates and prune correctly
        candidates.sort()
        
        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(curr_path.copy())
                return
            if curr_sum > target:
                return 

            for j in range(i, len(candidates)):
                # CRITICAL: Skip duplicates at the same decision level
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                # --- MAKE CHOICE ---
                curr_path.append(candidates[j])
                
                # --- RECURSE ---
                backtrack(j + 1, curr_sum + candidates[j])
                
                # --- UNDO CHOICE (Crucial fix!) ---
                curr_path.pop()
                
        backtrack(0, 0)
        return res