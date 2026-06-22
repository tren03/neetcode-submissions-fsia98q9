func trap(height []int) int {
	// precomp leftMax, rightMax
	type MaxVal struct{
		leftMax int
		rightMax int
	}
	arr := make([]MaxVal, len(height))
	
	var rev int
	var maxLeft int
	var maxRight int
	for i,_ := range height{
		rev = len(height) - 1 - i
		arr[i].leftMax = maxLeft
		arr[rev].rightMax = maxRight

		maxLeft = max(height[i], maxLeft)
		maxRight = max(height[rev], maxRight)
	}
	fmt.Println(arr)
	var ans int
	var waterAboveBar int
	for i, v := range height{
		waterAboveBar = max((min(arr[i].leftMax, arr[i].rightMax) - v),0)
		fmt.Println(waterAboveBar,arr[i].leftMax,arr[i].rightMax)
		ans += waterAboveBar
	}
	return ans
}
