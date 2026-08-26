class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        ind = 0
        i = 0
        least = len(t)
        while ind < len(s) - 1 and i <  len(t) - 1:
            while s[ind] != t[i] and ind < len(s) - 1:
                ind += 1
            print(s[ind], t[i])
            least = min(least, len(t) - i)
            i += 1
        
        return  least