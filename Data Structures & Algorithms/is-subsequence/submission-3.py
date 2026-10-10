class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        newS = set(s)
        i = 0
        j = 0
        while j < len(t):
            if s[i] == t[j]:
                i+= 1
                j += 1
            elif s[i] != t[j]:
                j+=1
            if i == len(s):
                return True

        return False