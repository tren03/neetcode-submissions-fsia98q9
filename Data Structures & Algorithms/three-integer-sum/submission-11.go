import "slices"
func threeSum(nums []int) [][]int {
	// sort asc
	ans := [][]int{}
	slices.SortFunc(nums, func(a, b int)int {
		switch {
			case b > a: 
				return -1
			case a > b:
				return 1
			default:
				return 0
		}
	})

	n := len(nums)
	m := 0
	for m <= n-1{
		target := -nums[m]
		left := m + 1
		right := n - 1
		for left < right{
			sum := nums[left] + nums[right]
			switch {
				case sum == target:
					ans = append(ans, []int{nums[m], nums[left], nums[right]})
					for left + 1 < n - 1  && nums[left+1] == nums[left]{
						left += 1
					}
					for right - 1 >= 0 && nums[right-1] == nums[right]{
						right -= 1
					}
					// increment both to find new values
					left += 1
					right -= 1
				case sum < target:
					left += 1
				default:
					right -= 1
			}
		}
		for m + 1 < n - 1 && nums[m+1] == nums[m]{
			m += 1
		}
		m += 1
	}
	return ans



}
