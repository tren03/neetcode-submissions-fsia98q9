func maxArea(heights []int) int {
	n := len(heights)
	left := 0
	right := n - 1
	ans := 0

	for left < right{
		l := heights[left]
		r := heights[right]
		area := (right - left) * min(l, r)
		ans = max(ans, area)
		fmt.Println(area, ans)
		switch {
			case l < r:
				left++
			default:
			 	right--
		}
	}
	return ans

}
