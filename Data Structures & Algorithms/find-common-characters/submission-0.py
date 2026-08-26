class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for w in words:
            cnt &= Counter(w)
        return list(cnt.elements())