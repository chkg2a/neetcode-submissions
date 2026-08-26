class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        f = count.most_common(1)[0][0]
        s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s:
                return [f,i]
        