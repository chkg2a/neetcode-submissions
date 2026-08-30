class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        if len(s) != len(t):
            return False
        for e,c in zip(s,t):
            if e not in sMap:
                sMap[e] = c
            if c not in tMap:
                tMap[c] = e
            if e != tMap[c] or sMap[e] != c:
                return False
        return True
            