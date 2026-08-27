class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #if len(cost) == 2:
        #    return min(cost)
        #dp = [0] * (len(cost)+1)
        #dp[-1] = 0
        #dp[-2] = cost[-1]
        #for i in range(len(cost)-2,-1,-1):
        #    dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        #return min(dp[0],dp[1])

        a = 0
        b = cost[-1]

        for i in range(len(cost)-2,-1,-1):
            x = cost[i] + min(a,b)
            a = b
            b = x

        return min(a,b)



        