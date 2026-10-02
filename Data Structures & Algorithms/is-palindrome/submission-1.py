class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = "".join(s.split())
        res = ""
        for c in strs:
            if c.isalnum():
                res += c.lower()
        print(res)
        return res == res[::-1]