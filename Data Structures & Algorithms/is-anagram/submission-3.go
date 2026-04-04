func isAnagram(s string, t string) bool {
	sMap := make(map[rune]int)
	for _, val := range s{
		sMap[val] += 1
	}

	for _, val := range t{
		v, ok := sMap[val]
		if !ok{
			return false
		}
		if v == 1{
			delete(sMap, val)
			continue
		}
		sMap[val] = v-1
	}

	if len(sMap) == 0{
		return true
	}
	return false
}
