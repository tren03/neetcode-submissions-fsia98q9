func minEatingSpeed(piles []int, h int) int {
	var timetaken func(int) int // takes eating rate and provides hours taken
	timetaken = func(rate int)int{
		hours := 0
		for _, val  := range piles{
			if rate >= val{
				hours++
			}else{
				if val % rate == 0{
					hours += (val / rate)
				}else{
					hours += (val / rate) + 1
				}
			}
		}
		return hours
	}
	
	maxHours := 0
	minHours := 1
	for _, val := range piles{
		maxHours = max(val, maxHours)
	}
	ans := maxHours

	// search space = [minHours, maxHours], 
	for minHours <= maxHours{
		rateToCheck := (minHours + maxHours) / 2
		fmt.Println(minHours, maxHours, rateToCheck, timetaken(rateToCheck))
		if timetaken(rateToCheck) <= h{
			// probable answer
			ans = min(rateToCheck, ans)
			maxHours = rateToCheck - 1
		}else{
			minHours = rateToCheck + 1
		}
	}
	return ans

}
