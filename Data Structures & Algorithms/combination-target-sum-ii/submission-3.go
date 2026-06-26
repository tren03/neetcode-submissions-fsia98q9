import "slices"
func combinationSum2(candidates []int, target int) [][]int {
    var rec func(int, int, []int)
    ans := make([][]int, 0)

    slices.SortFunc(candidates, func(a int,b int)int{
        return a - b
    })


    rec = func(i int, sum int, temp[]int){
        if sum == target{
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }
        if i >= len(candidates){
            return
        }
        if sum > target{
            return
        }

        // 1. include element
        temp = append(temp, candidates[i])
        rec(i+1, sum+candidates[i], temp)

        // 2. skip dups and call next func with old sum/temp
        temp = temp[:len(temp)-1]
        // find next distinct index
        o := candidates[i]
        i += 1
        for ;i<len(candidates);i+=1{
            if candidates[i] != o{
                break
            }
        }
        rec(i, sum, temp)
    }
    rec(0,0,[]int{})
    return ans
}
