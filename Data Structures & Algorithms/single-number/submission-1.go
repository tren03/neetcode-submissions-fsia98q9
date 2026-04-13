func singleNumber(nums []int) int {
	ans := nums[0]
	for i := 1; i < len(nums); i+=1{
		ans = ans ^ nums[i]
	}
	return ans
}
