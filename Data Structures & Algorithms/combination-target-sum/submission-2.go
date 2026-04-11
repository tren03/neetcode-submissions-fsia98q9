import "slices"
func combinationSum(candidates []int, target int) [][]int {
    ans := make([][]int, 0)
    var r func(int, int, []int)

    r = func(ind int, s int, temp []int){
        if ind >= len(candidates){
            return
        }
        if s == target{
            c := make([]int, len(temp))
            copy(c, temp)
            ans = append(ans, c)
            return
        }
        if s > target{
            return
        }
        temp = append(temp, candidates[ind])
        r(ind, s+candidates[ind], temp)
        temp = slices.Delete(temp, len(temp)-1, len(temp))
        r(ind+1, s, temp)
    }
    r(0,0,[]int{})
    return ans
    
}