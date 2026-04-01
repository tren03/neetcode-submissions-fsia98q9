func maxProfit(prices []int) int {
	n := len(prices)
	left := 0
	right := 0
	profit := 0

	for right < n{
		curProfit := prices[right] - prices[left]
		fmt.Println(left, right, profit, curProfit)
		profit = max(profit, curProfit)
		for curProfit < 0 && left < right{
			left += 1
		}
		right += 1
	}
	return profit
}
