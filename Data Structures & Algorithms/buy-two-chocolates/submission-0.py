class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        secondMin = 10000000
        mini = 10000000
        for i in prices:
            if i < mini:
                secondMin = mini
                mini = i
            elif secondMin > i:
                secondMin = i
        if (money - mini - secondMin) < 0:
            return money
        else:
            return (money - mini - secondMin)