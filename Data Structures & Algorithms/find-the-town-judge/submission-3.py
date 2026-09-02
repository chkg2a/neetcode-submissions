class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s = set()
        cnt = defaultdict()

        for i in range(len(trust)):
            s.add(trust[i][0])
            cnt[trust[i][1]] = 1 + cnt.get(trust[i][1],0)
        for i in range(1,n+1):
            if i not in s and i in cnt and cnt[i] == n - 1:
                return i
        return -1