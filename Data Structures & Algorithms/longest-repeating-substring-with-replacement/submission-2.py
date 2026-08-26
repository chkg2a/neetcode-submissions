class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        highest = 1
        i = 0
        j = 1
        still_possible = k
        longest = 1
        count = Counter(s)
        current_char = count.most_common()[0][0]
        while j < len(s):
            if current_char == s[j]:
                longest += 1
            elif current_char != s[j] and still_possible > 0:
                longest += 1
                still_possible -= 1
            else:
                longest = 1
                still_possible = min(k,still_possible + 1)
                i += 1
                current_char = s[i]
            j += 1
            highest = max(longest, highest)
        return highest
