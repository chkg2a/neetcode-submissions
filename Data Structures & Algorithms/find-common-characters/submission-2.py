class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])

        for word in words:
            current_cnt = Counter(word)
            for c in cnt:
                cnt[c] = min(cnt[c], current_cnt[c])
        
        res = []
        for i in cnt:
            for j in range(cnt[i]):
                res.append(i)
        return res
                

