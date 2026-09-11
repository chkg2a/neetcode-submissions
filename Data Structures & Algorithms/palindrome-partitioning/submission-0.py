class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def backtrack(j,i):
            if i >= len(s):
                if j == i:
                    res.append(subset.copy())
                return
            if self.isPalin(s,j,i):
                subset.append(s[j:i+1])
                backtrack(i+1,i+1)
                subset.pop()
            backtrack(j,i+1)
            
                
        backtrack(0,0)
        return res

    def isPalin(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True