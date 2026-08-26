class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        j = 0
        i = 0
        still_possible = k
        count = Counter(s)
        current_char = count.most_common()[0][0]
        highest = 0
        longest = highest
        while j < len(s):
            if current_char == s[j]:
                longest += 1
            elif current_char != s[j] and still_possible > 0:
                longest += 1
                still_possible -= 1
            else:
                longest = 0
                while s[i] != current_char:
                    i += 1
            j += 1
            highest = max(longest, highest)
        return highest
