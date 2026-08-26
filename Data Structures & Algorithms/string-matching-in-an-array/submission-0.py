class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        op = set()

        for word in words:
            for sub in words:
                if word in sub and word != sub:
                    op.add(word)
        return list(op)