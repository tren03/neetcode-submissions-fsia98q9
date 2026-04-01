func climbStairs(n int) int {
	// explore all paths starting from n
	var rec func(int) int
	dp := make([]int, n+1)

	// initialize to -1 for unfound items
	for ind, _ := range dp{
		dp[ind] = -1
	}
	rec = func(n int)int{
		if n == 0 || n == 1{
			return 1
		}
		small := dp[n-2]
		if small == -1{
			small =rec(n-2) 
			dp[n-2] = small
		}
		big := dp[n-1]
		if big == -1{
			big =rec(n-1) 
			dp[n-1] = big
		}
		return big + small
	}
	return rec(n)
    
}
