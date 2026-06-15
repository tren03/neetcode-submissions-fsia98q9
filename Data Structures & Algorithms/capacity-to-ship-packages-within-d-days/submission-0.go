func dayCalc(w []int, capacity int)int{
	t := 0
	days := 1
	for _, v := range w{
		if t + v > capacity{
			days += 1
			t = v
		}else{
			t += v
		}
	}
	return days

}
func shipWithinDays(weights []int, days int) int {
	l := weights[0]
	r := 0
	for _,v := range weights{
		r += v
		l = max(l, v)
	}
	ans := r
	fmt.Println(l,r)
	for l<=r{
		mid := (l+r)/2
		probableDays := dayCalc(weights, mid)
		fmt.Println("max weight",mid)
		fmt.Println("days with max weight",probableDays)
		if probableDays == days{
			fmt.Println(ans)
			ans = mid
			r = mid - 1
			continue
		}
		if probableDays < days{
			ans = min(ans, mid)
			fmt.Println("ans", ans)
			r = mid - 1
		}else{
			l = mid + 1

		}
	}
	fmt.Println(ans)
	return ans

	


}
