class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for word in words:
            current_count = Counter(word)
            for c in cnt:
                cnt[c] = min(cnt[c],current_count[c])
        
        res = []
        for c in cnt:
            for i in range(cnt[c]):
                res.append(c)
        return res