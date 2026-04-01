func productExceptSelf(nums []int) []int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	ans := make([]int, n)

	//left := [n]int{}
	//right := [n]int{}
	//ans :=  [n]int{}
	for i, _ := range nums{
		if i == 0{
			//left = append(left, 1)
			left[i] = 1
			continue
		}
		//left = append(left, nums[i-1]*left[i-1])
		left[i] = nums[i-1] * left[i-1]
	}
	fmt.Println(left)
	for i := len(nums)-1; i>=0; i--{
		if i == len(nums)-1{
			//right = append(right, 1)
			right[i] = 1
			continue
		}
		//right = append(right, right[i-1] * nums[i+1])
		right[i] = right[i+1] * nums[i+1]
	}
	for i:=0; i<len(nums);i++{
		ans[i] = left[i] * right[i]
	}
	fmt.Println(left)
	fmt.Println(right)
	return ans

}
