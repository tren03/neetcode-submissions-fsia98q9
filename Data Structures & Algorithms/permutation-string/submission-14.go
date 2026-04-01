import "maps"
func checkInclusion(s1 string, s2 string) bool {
	m1 := make(map[byte]int)
	m2 := make(map[byte]int)
	left := 0
	right := 0
	for _, v := range s1{
		m1[byte(v)]++
	}

	fmt.Println(len(s1))
	for right < len(s2){
		if right < len(s1){
			m2[s2[right]]++
			right++
			fmt.Println("inside",m1, m2)
			// check Perm
			if maps.Equal(m1, m2){
				return true
			}
			continue
		}else{
			// increment both pointers
			if m2[s2[left]] == 1{
				delete(m2, s2[left])
			}else{
				m2[s2[left]]--
			}
			left++

			m2[s2[right]]++
			right++
		}
		if maps.Equal(m1, m2){
			return true
		}

	}
	fmt.Println(m1, m2)
	return false
}
