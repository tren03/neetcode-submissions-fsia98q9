func rob(nums []int) int {
    dp := make([]int, len(nums))
    dp[len(nums)-1] = nums[len(nums)-1]
    ans := nums[len(nums)-1]
    for i := len(nums) - 2; i >= 0; i -= 1{
        otherMaxInd := i + 2
        otherMax := 0
        if !(otherMaxInd >= len(nums)){
            otherMax = dp[otherMaxInd]
        }
        dp[i] = max(dp[i+1], nums[i] + otherMax)
        ans = max(ans, dp[i])
    }
    return ans
}