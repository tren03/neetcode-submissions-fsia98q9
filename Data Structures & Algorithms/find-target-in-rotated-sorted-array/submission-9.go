func search(nums []int, target int) int {

	var bs func([]int)int
	bs = func (n []int)int{
		left := 0
		right := len(n)-1
		for right >= left{
			mid := (left + right)/2
			val := n[mid]
			if val == target{
				return mid
			}else if val > target{
				right = mid - 1
			}else{
				left = mid + 1
			}
		} 
		return -1
	}

	left := 0
	right := len(nums) - 1
	mid := (left + right)/2
	// if array is fully sorted, just normal binary search
	if nums[left] <= nums[mid] && nums[right] >= nums[mid]{
		return bs(nums)
	}

	for left <= right{
		mid := (left + right)/2
		if nums[mid] == target{
			return mid
		}
		if nums[left] <= nums[mid]{
			// left is sorted half
			if (target >= nums[left] && target <= nums[mid]){
				// eliminate right
				right = mid - 1
			}else{
				// eliminate left
				left = mid + 1
			}
		}else{
			// right is sorted
			if (target >= nums[mid] && target <= nums[right]){
				// eliminate left
				left = mid + 1
			}else{
				// eliminate right
				right = mid - 1
			}
		}
		
	}
	return -1

}


