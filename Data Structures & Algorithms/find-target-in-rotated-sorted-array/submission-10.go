func search(nums []int, target int) int {

	left := 0
	right := len(nums) - 1

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


