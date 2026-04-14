import "slices"
import "cmp"
func combinationSum2(candidates []int, target int) [][]int {
    slices.SortFunc(candidates, func(a,b int) int{
        return cmp.Compare(a,b)
    })
    var r func([]int, int, int)
    ans := make([][]int, 0)
    fmt.Println(candidates)

    r = func(temp []int, s int, i int){
        if s == target{
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }
        if i >= len(candidates) || s > target{
            return
        }
        temp = append(temp, candidates[i])
        r(temp, s+candidates[i], i+1)
        for {
            t := i + 1
            if !(t >= len(candidates)){
                if candidates[t] == candidates[i]{
                    i = i + 1
                }else{
                    break
                }
            }else{
                break
            }
        }
        temp = slices.Delete(temp, len(temp)-1, len(temp))
    r(temp, s, i+1)
    }
    r([]int{}, 0, 0)
    return ans
}