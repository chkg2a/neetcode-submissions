class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd_freq = 0
        even_freq = 1000000
        ans = -100000
        for i in cnt:
            if cnt[i] % 2 == 0:
                even_freq = min(even_freq,cnt[i])
            if cnt[i] % 2 == 1:
                odd_freq = max(odd_freq,cnt[i])
        ans = max(ans,odd_freq - even_freq)
        return ans