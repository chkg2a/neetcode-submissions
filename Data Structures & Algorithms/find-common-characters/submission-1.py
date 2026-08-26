class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c = Counter(words[0])
        ans = []
        for i in words:
            w = Counter(i)
            for key, val in c.items():
                if w[key] == 0:
                    c[key] = 0
                else:
                    c[key] = min(c[key], w[key])
        for key, val in c.items():
            if val > 0:
                ans.extend([key]*val)

        return ans