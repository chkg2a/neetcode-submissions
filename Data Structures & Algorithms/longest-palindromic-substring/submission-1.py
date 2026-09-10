class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""
        i = 0
        def checker(l,r):
            nonlocal resLen, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        while i < len(s):
            checker(i,i)
            checker(i,i+1)
            i+=1
        return res
