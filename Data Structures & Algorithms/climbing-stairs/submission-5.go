func climbStairs(n int) int {
	var dfs func(int) int
	dp := make(map[int]int,0)
	dfs = func(step int) int{
		if step == n{
			return 1
		}
		if step > n{
			return 0
		}
		if v,ok := dp[step]; ok{
			return v
		}
		left := dfs(step+1)
		right := dfs(step+2)
		dp[step] = left+right
		return left + right
	}
	return dfs(0)
}
