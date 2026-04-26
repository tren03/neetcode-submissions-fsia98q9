func climbStairs(n int) int {
	dp := make([]int, n)
	dp[n-1] = 1
	for i := n-2; i >= 0; i -= 1{
		// 2 ways - 1 step taken / 2 step taken
		// 1 + dp[i+1] + 1 + dp[i+2]
		firstChoice := 0
		secondChoice := 0

		if i + 1 == n{
			firstChoice = 1
		}else if i + 1 < n{
			firstChoice = dp[i+1]
		}

		if i + 2 == n{
			secondChoice = 1
		}else if i + 1 < n{
			secondChoice = dp[i+2]
		}

		dp[i] = firstChoice + secondChoice
	}
	return dp[0]
    
}
