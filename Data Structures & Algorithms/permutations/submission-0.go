func permute(nums []int) [][]int {
	if len(nums) == 0{
		return [][]int{}
	}

	temp := []int{}
	truth := make([]bool, len(nums)) // if false, number taken
	ans := [][]int{}
	var rec func([]int,  []bool)

	rec = func(temp []int, truth []bool){
		fmt.Println(temp, truth)
		if len(temp) == len(nums){
			d := make([]int, len(nums))
			copy(d, temp)
			ans = append(ans, d)
			return
		}

		fmt.Println("truth_table", truth)
		for ind, v := range truth{
			if v == false{
				truth[ind] = true
				temp = append(temp, nums[ind])
				rec(temp, truth)

				// undo steps to move state upward in tree
				temp = temp[:len(temp)-1]
				truth[ind] = false
			}
		}
	}

	rec(temp, truth)
	return ans
}
