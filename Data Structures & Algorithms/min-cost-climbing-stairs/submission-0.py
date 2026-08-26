class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        l = [0] * (n + 1)

        for i in range(2,n + 1):
            option1 = l[i - 1] + cost[i - 1]
            option2 = l[i - 2] + cost[i - 2]
            l[i] = min(option1, option2)
        
        return l[n]