class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        count = 0
        for word in words:
            c_cnt = Counter(word)
            failed = False
            for c in c_cnt:
                if c_cnt[c] > cnt[c]:
                    failed = True
            if failed == False:
                count+= len(word)
        return count