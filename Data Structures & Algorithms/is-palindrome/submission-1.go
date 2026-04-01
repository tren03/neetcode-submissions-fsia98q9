func isPalindrome(s string) bool {
	// perform conversion
	sArr := strings.Split(s," ")
	for i,v := range sArr{
		sArr[i] = strings.ToLower(v)
	}
	sClean := strings.Join(sArr,"")
	sFinal := ""
	for _, char := range sClean{
		condition := (char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9')
		if condition{
			sFinal += string(char)
		}
	}

	i:=0
	j:=len(sFinal)-1
	for {
		if i>j{
			break
		}
		if sFinal[i] == sFinal[j]{
			i++
			j--
		}else{
			return false
		}

	}
	return true
	
}
