func maxSubArray(nums []int) int {
	ans := nums[len(nums)-1]
	rs := ans
	for i:=len(nums)-2;i>=0;i-=1{
		cur := nums[i]
		if rs < 0{
			rs = cur
		}else{
			rs = cur + rs
		}
		ans = max(ans, rs)
	}
	return ans
}
