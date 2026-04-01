func characterReplacement(s string, k int) int {
	// checking validity 
	// array of letters -> k  - maxOccurance >= 0
	left := 0
	right := 0
	ans := 0
	m := make(map[byte]int)
	n := len(s)
	maxCount := 0
	for right < n{
		fmt.Println(checkValidity(m,left,right,k, maxCount), left, right)
		m[s[right]] += 1
		maxCount = max(m[s[right]], maxCount)
		for checkValidity(m,left,right,k,maxCount) == false && left <= right{
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

func checkValidity(m map[byte]int, i,j,k,maxCount int) bool{
	if ((j-i)+1) - maxCount <= k{
		return true
	}
	return false
}