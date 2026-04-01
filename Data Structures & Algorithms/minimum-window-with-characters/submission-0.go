func minWindow(s string, t string) string {
	smap := make(map[byte]int)
	tmap := make(map[byte]int)

	for _, v := range t{
		tmap[byte(v)] += 1
	}
	left := 0
	right := 0
	match := 0
	ans := ""
	minLength := math.MaxInt
	fmt.Println(len(tmap))

	for right < len(s){
		// ADDITION PHASE (increase match)
		cur := s[right]
		if _, ok := tmap[cur]; ok{
			if smap[cur] + 1 == tmap[cur]{
				match++
			}
		}else{
			// we do not care do nothing
		}
		smap[cur]++
		
		// SHRINK PHASE, to get probable match (match can never be greater than len(t), since we always check this)
		// once we increase match
		for match == len(tmap){
			// log ans everytime we shrink as it might be a new answer, only if smaller than logged min
			if (right - left) < minLength{
				ans = s[left:right+1]
				minLength = (right - left) + 1
			}
			popVal := s[left]
			if _, ok := tmap[popVal]; ok{
				if smap[popVal] - 1 < tmap[popVal]{
					match--
				}
			}
			smap[popVal]--
			left++
			// shrink left until map invalid
		}
		right++
	}
	return ans

}
