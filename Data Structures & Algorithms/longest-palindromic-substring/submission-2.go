func longestPalindrome(s string) string {
	ans := ""

	for i := 0; i<len(s);i+=1{
		// odd case
		l, r := i,i
		for l >= 0 && r < len(s) && s[l] == s[r]{
			if len(s[l:r+1]) > len(ans){
				ans = s[l:r+1]
			}
			l -= 1
			r += 1
		}

		// even case
		l,r = i, i+1
		for l >= 0 && r < len(s) && s[l] == s[r]{
			if len(s[l:r+1]) > len(ans){
				ans = s[l:r+1]
			}
			l -= 1
			r += 1
		}
	}
	return ans
}
