/* 
[]
[2] []
[2,2] [2,5] [5] []
[2,2,2] [2,5,6] [2,5,5] [2,5,6] [5,5] [5,6] [6] []
*/
import "slices"

var rec func([]int, int, int)
func combinationSum(nums []int, target int) [][]int {
	temp := []int{}
	i := 0
	sum := 0
	ans := [][]int{}


	rec = func(temp []int, i int, sum int){
		if sum > target || i >= len(nums){
			return
		}
		if sum == target{
			d := make([]int, len(temp))
			copy(d, temp)
			ans = append(ans, d)
			return
		}
		temp = append(temp, nums[i])
		sum += nums[i]
		rec(temp, i, sum)
		temp = slices.Delete(temp, len(temp)-1, len(temp))
		sum -= nums[i]
		rec(temp, i+1, sum)
	}

	rec(temp, i, sum)
	return ans
    
}
