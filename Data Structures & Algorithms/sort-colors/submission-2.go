func sortColors(nums []int) {
	l := 0
	r := len(nums) - 1
	i := 0

	for i <= r{
		if nums[i] == 0{
			nums[i] , nums[l] = nums[l], nums[i]
			l += 1
			i += 1
		}else if nums[i] == 2{
			nums[i] , nums[r] = nums[r], nums[i]
			r -= 1
		}else{
			i += 1
		}
	}

}
