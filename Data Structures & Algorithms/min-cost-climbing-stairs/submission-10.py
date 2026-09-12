class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        a = cost[-1]
        b = 0
        for i in range(n-2,-1,-1):
            cur = cost[i] + min(a,b)
            b = a
            a = cur
        return min(a,b)



        