class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        ind = 0
        i = 0
        least = len(t)
        while ind < len(s) and i <  len(t):
            while s[ind] != t[i] and ind < len(s) - 1:
                ind += 1
            least = min(least, len(t) - i)
            ind += 1
            i += 1
        
        return  least