func hasDuplicate(nums []int) bool {
	m := make(map[int]bool)
	for _, val := range nums{
		_, ok := m[val]
		if ok == true{
			return true
		}
		m[val] = true
	}
	return false
	
    
}
