func findMin(nums []int) int {
	left := 0
	right := len(nums)-1
	ans := math.MaxInt
	for left <= right{
		mid := (left + right)/2

		fmt.Println(left, right, nums[mid])
		if nums[left] <= nums[mid]{
			ans = min(ans, nums[left])
			left = mid + 1
		}
		if nums[right] >= nums[mid]{
			ans = min(ans, nums[mid])
			right = mid - 1
		}
	}
	return ans

}
