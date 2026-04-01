/*
if we sort the arr
922 -> 229
[]

*/
import "slices"
var rec func([]int, int, int)
func combinationSum2(candidates []int, target int) [][]int {
	temp := []int{}
	i, sum := 0, 0
	ans := [][]int{}

	slices.SortFunc(candidates, func(a,b int) int{
		return b - a
	})

	rec = func(temp []int, i int, sum int){
		if sum == target{
			d := make([]int, len(temp))
			copy(d, temp)
			ans = append(ans, d)
			return
		}
		if sum > target || i >= len(candidates){
			return
		}
		fmt.Println(temp)
		sum += candidates[i]
		temp = append(temp, candidates[i])
		rec(temp, i+1, sum) // pass next as we do not include same var twice
		// prevent reprocess of duplicates
		sum -= candidates[i]
		temp = temp[:len(temp)-1]
		for i < len(candidates) - 1 && candidates[i] == candidates[i+1]{
			i += 1
		}
		rec(temp, i+1, sum)
	}
	rec(temp, i, sum)
	return ans
}
