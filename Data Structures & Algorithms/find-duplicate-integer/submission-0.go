func findDuplicate(nums []int) int {
	// ptr = value of nums, val = ind of nums
	slow := 0
	fast := 0
	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast{
			break
		}
	}
	slow = 0
	for fast != slow{
		slow = nums[slow]
		fast = nums[fast]
	}
	return fast
}

