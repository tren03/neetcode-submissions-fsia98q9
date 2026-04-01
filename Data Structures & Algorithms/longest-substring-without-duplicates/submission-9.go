func lengthOfLongestSubstring(s string) int {
	left := 0
	right := 0
	ans := 0
	m := make(map[byte]struct{})

	for right < len(s){
		for {
			_, ok := m[s[right]]
			if !ok{
				break
			}
			delete(m, s[left])
			left++
		}
		m[s[right]] = struct{}{}
		ans = max(ans, len(m))
		right++
	}
	return ans


}
