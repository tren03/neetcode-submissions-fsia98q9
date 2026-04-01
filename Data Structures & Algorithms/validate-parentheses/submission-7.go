import "slices"
func isValid(s string) bool {
	m := map[rune]rune{
		'{':'}',
		'[':']',
		'(':')',
	}
	st := []rune{}

	for _,char := range s{
		if _, ok := m[rune(char)]; ok{
			st = append(st,rune(char))
		}else{
			if len(st) > 0 && m[st[len(st)-1]] == rune(char){
				st = slices.Delete(st, len(st)-1, len(st))
			}else{
				return false
			}
		}
		fmt.Println(st)
	}
	if len(st) == 0{
		return true
	}
	return false
}
