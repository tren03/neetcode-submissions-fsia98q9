func hs(arr []int)int{
	if len(arr) == 1{
		return arr[0]
	} 
	if len(arr) == 2{
		return max(arr[0], arr[1])
	}
	dp := make([]int, len(arr))
	ans := 0
	dp[len(arr)-1] = arr[len(arr)-1]
	dp[len(arr)-2] = max(arr[len(arr)-2], arr[len(arr)-1])
	ans = max(dp[len(arr)-1], dp[len(arr)-2])
	for i := len(arr)-3; i >= 0; i-=1{
		fmt.Println("dp",dp)
		dp[i] = max(arr[i] + dp[i+2], dp[i+1] )// rob house | skip house (if skip max is the max of next)
		ans = max(ans, dp[i])
	}
	fmt.Println("dp",dp)
	return ans
	
}
func rob(nums []int) int {
	if len(nums) == 0{
		return 0
	}
	if len(nums) == 1{
		return nums[0]
	}
	l := nums[:len(nums)-1]
	r := nums[1:len(nums)]
	fmt.Println(l,r)
	return max(hs(l), hs(r))
}
