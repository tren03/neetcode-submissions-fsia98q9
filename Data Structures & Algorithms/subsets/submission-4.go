import "slices"
func subsets(nums []int) [][]int {
    ans := make([][]int,0)

    var rec func(int, []int)

    rec = func(i int, temp []int){
        if i == len(nums){
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }

        // include
        temp = append(temp, nums[i])
        rec(i+1,temp)
        temp = slices.Delete(temp,len(temp)-1,len(temp))
        rec(i+1, temp)
    }
    rec(0,[]int{})

    return ans

}
