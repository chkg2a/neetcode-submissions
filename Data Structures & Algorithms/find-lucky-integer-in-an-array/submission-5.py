class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt= Counter(arr)
        highest = -1
        for i in arr:
            if cnt[i] == i:
                highest = max(cnt[i],highest)
        return -1 if highest == -1  else highest