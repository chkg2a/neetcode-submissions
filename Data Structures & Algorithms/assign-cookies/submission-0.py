class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        l = set(g)
        for i in s:
            if i in l:
                count += 1 
                l.remove(i)
        return count