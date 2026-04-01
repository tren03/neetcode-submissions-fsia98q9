func characterReplacement(s string, k int) int {
	// checking validity 
	// array of letters -> k  - maxOccurance >= 0
	left := 0
	right := 0
	ans := 0
	m := make(map[byte]int)
	n := len(s)
	for right < n{
		fmt.Println(checkValidity(m,left,right,k), left, right)
		m[s[right]] += 1
		for checkValidity(m,left,right,k) == false && left <= right{
			if v,_ := m[s[left]]; v == 0{
				delete(m, s[left])
			}else{
				m[s[left]]--
			}
			left++
		}
		ans = max(ans, (right-left)+1)
		right++
	}
	return ans

}

func checkValidity(m map[byte]int, i,j,k int) bool{
	maximum := 0
	for _, val := range m{
		maximum = max(maximum, val)
	}
	if ((j-i)+1) - maximum <= k{
		return true
	}
	return false
}