class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        for c in s:
            mp[c] = 1 + mp.get(c,0)
        for c in t:
            mp[c] = mp.get(c,0) - 1
        
        for c in mp:
            if mp[c] < 0:
                return c
        return ""