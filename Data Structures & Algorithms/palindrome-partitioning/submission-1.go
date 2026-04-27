import "slices"
func isPalindrome(s string, m map[string]bool)bool{
	if v, ok := m[s]; ok{
		return v
	}
	end := len(s) - 1
	start := 0
	for start <= end{
		if s[start] != s[end]{
			m[s] = false
			return false
		}
		start += 1
		end -= 1
	}
	m[s] = true
	return true
}
func partition(s string) [][]string {
	var dfs func(int, []string)
	ans := make([][]string, 0)
	m := make(map[string]bool)
	
	dfs = func(start int, temp []string){
		if start == len(s){
			t := make([]string, len(temp))
			copy(t, temp)
			ans = append(ans, t)
			return
		}

		for i := start + 1; i <= len(s); i += 1{
			split := string([]byte(s[start:i]))
			isPal := isPalindrome(split,m)
			if !isPal{
				continue
			}
			temp = append(temp, split)
			dfs(i, temp)
			temp = slices.Delete(temp, len(temp)-1,len(temp))
		}

	}
	dfs(0,[]string{})
	return ans
}
