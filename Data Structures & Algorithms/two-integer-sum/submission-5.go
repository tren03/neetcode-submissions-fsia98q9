func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for ind, val := range nums{
		t := target - val
		if v, ok := m[t]; ok && ind != v{
			return []int{v, ind}
		}
		m[val] = ind
	}
	return []int{1, 2}
}
