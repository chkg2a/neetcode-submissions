class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        upper_arr = [0] * 26
        for i in s:
            indx = ord(i) - ord("A")
            upper_arr[indx] += 1
        highest = 0
        for i in range(26):
            if highest < upper_arr[i]:
                highest = upper_arr[i]
        return min(len(s), highest + k)
