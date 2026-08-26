class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        maxVal = 0

        maxVal = min(count['b'], count['a'],count['l'] // 2,count['o'], count['n'])
        print(count['b'])
        print(count['a'])
        print(count['l'])
        print(count['o'])
        print(count['n'])
        return maxVal