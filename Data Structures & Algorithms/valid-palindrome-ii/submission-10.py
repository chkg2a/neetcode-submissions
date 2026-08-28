class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        count = 0
        while i < j:
            if s[i] != s[j]:
                skipI = s[i+1:j+1]
                skipJ = s[i:j]
                return (skipI == skipI[::-1] or skipJ == skipJ[::-1])
            i += 1
            j -= 1
        return True