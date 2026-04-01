func evalRPN(tokens []string) int {
	s := []int{}

	for _, token := range tokens{
		tokenInt, err := strconv.Atoi(string(token))
		if err == nil{
			s = append(s, tokenInt)
		}else{
			switch token{
				case "+": 
					fmt.Println(token, s)
					a := s[len(s)-1]
					b := s[len(s)-2]
					s = s[:len(s)-2]
					s = append(s, b+a)
				case "-": 
					a := s[len(s)-1]
					b := s[len(s)-2]
					s = s[:len(s)-2]
					s = append(s, b-a)
				case "*": 
					a := s[len(s)-1]
					b := s[len(s)-2]
					s = s[:len(s)-2]
					s = append(s, b*a)
				case "/": 
					a := s[len(s)-1]
					b := s[len(s)-2]
					s = s[:len(s)-2]
					s = append(s, b/a)
			}

		}
		fmt.Println(token, s)

	}
	return s[len(s)-1]

}
