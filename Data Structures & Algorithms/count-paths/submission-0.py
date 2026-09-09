class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i].append(0)
        dp[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j==n-1:
                    print("skip")
                    continue
                a = 0
                b = 0
                if i+1 < m and i >= 0:
                    a = dp[i+1][j]
                if j+1 < n and j >= 0:
                    b = dp[i][j+1]
                dp[i][j] = a+b
                print(i,j,dp[i][j])
        return dp[0][0]


        