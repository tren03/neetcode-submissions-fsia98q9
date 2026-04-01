func dailyTemperatures(temperatures []int) []int {
	st := [][]int{} // [(value, index)]
	ans := make([]int, len(temperatures))

	for ind, val := range temperatures{
		if len(st) == 0{
			st = append(st, []int{val, ind})
			continue
		}
		headVal := st[len(st)-1][0]
		headInd := st[len(st)-1][1]

		if val <= headVal{
			st = append(st, []int{val, ind})
			continue
		}

		for len(st) > 0 && val > st[len(st)-1][0]{
			headInd = st[len(st)-1][1]
			ans[headInd] = ind - headInd
			st = st[:len(st)-1]
		}
		st = append(st, []int{val, ind})
	}
	return ans
}
