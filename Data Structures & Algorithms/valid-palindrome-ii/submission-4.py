class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        count = 0
        while i < j:
            if s[i] != s[j] and (s[i + 1] != s[j] and s[i] != s[j-1]) and count == 0:
                return False
            if s[i] != s[j]:
                count += 1
            i += 1
            j -= 1

        return True
