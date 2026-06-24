import "slices"
func combinationSum(nums []int, target int) [][]int {
    var rec func(int, int, []int)
    ans := make([][]int, 0)

    rec = func(i int, s int, arr []int){
        if s == target{
            t := make([]int, len(arr))
            copy(t, arr)
            ans = append(ans, t)
            return
        }
        if s > target{
            return
        }
        if i >= len(nums){
            return
        }

        arr = append(arr, nums[i])
        rec(i, s+nums[i], arr)

        arr = slices.Delete(arr, len(arr)-1, len(arr))
        rec(i+1, s, arr)
    }
    rec(0,0,[]int{})

    return ans
}

