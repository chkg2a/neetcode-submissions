class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        count = 0
        while i < j:
            if s[i] != j[i]:
                count +=1
            i += 1
            j -= 1
        return True if count <= 0 else False