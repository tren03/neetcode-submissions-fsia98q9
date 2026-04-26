func climbStairs(n int) int {
	if n == 1{
		return 1
	}
	dp := make([]int, n)
	dp[n-1] = 1
	dp[n-2] = 2
	for i := n-3; i >= 0; i -= 1{
		// 2 ways - 1 step taken / 2 step taken
		// 1 + dp[i+1] + 1 + dp[i+2]
		firstChoice := dp[i+1] 
		secondChoice := dp[i+2] 
		dp[i] = firstChoice + secondChoice
	}
	return dp[0]
    
}
