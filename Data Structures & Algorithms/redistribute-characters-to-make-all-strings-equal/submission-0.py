class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = Counter("".join(words))
        num_words = len(words)
        return all(c % num_words == 0 for c in cnt.values())
