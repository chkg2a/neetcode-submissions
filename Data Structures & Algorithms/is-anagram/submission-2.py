class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        cc = Counter(t) 
        return c == cc