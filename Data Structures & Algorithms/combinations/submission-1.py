class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        current_path = []
        def backtrack(i):
            if len(current_path) == k:
                res.append(current_path.copy())
                return

            for j in range(i,n+1):
                current_path.append(j)
                backtrack(j+1)
                current_path.pop()
        backtrack(1)
        return res