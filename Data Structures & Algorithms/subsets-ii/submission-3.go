import "slices"
func subsetsWithDup(nums []int) [][]int {
    var rec func([]int, int)

    slices.SortFunc(nums, func(a,b int)int{
        return a-b
    })

    ans := make([][]int, 0)

    rec = func(temp[]int, i int){
        if i >= len(nums){
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }
        // include ele
        temp = append(temp, nums[i])
        rec(temp, i+1)

        // remove ele
        temp = temp[:len(temp)-1]
        original := nums[i]
        i=i+1
        for ;i<len(nums);i++{
            if nums[i] != original{
                break
            }
        }
        rec(temp, i)
    }
    rec([]int{},0)
    return ans

}
