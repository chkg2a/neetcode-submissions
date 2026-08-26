class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        maxVal = 0

        maxVal = min(count['b'], count['a'],count['l'] * 2,count['o'], count['n'])
        return maxVal