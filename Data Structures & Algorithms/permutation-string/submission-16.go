func checkPerm(a string, b string) bool{
	fmt.Println(a,b)
	if len(a) != len(b){
		return false
	}
	o := make(map[rune]int)
	for _, v := range a{
		o[v] += 1
	}

	for _, v := range b{
		if _, ok := o[v]; !ok{
			return false
		}
		if o[v] == 1{
			delete(o, v)
			continue
		}
		o[v] -= 1
	}
	if len(o) == 0{
		return true
	}
	return false
}
func checkInclusion(s1 string, s2 string) bool {
	l := 0
	r := len(s1) - 1
	if r > len(s2)-1{
		return false
	}
	for r <= len(s2)-1{
		if checkPerm(s2[l:r+1], s1) == true{
			return true
		}
		r += 1
		l += 1
	}
	return false
}
