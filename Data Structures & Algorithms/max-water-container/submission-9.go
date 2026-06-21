func maxArea(heights []int) int {
	// area = min(heights[l],heights[r]) * r-l
	l := 0
	r := len(heights) - 1
	ans := 0
	for r > l{
		area := min(heights[l], heights[r]) * (r-l)
		ans = max(area, ans)
		if heights[l] < heights[r]{
			l += 1
		}else{
			r-=1
		}
	}
	return ans
}
