import "slices"
import "cmp"
func subsetsWithDup(nums []int) [][]int {
    slices.SortFunc(nums, func(a,b int)int{
        return cmp.Compare(a,b)
    })
    fmt.Println(nums)

    var r func([]int, int)
    ans := make([][]int, 0)

    r = func(temp []int, ind int){
        if ind >= len(nums){
            fmt.Println(len(temp))
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }
        temp = append(temp, nums[ind])
        r(temp, ind+1)
        temp = slices.Delete(temp, len(temp)-1, len(temp))

        toCheck := nums[ind]
        for {
            t := ind + 1
            if t < len(nums) && nums[t] == toCheck{
                ind += 1
            }else{
                break
            }
        }

        r(temp, ind+1)
    }
    r([]int{}, 0)
    return ans
}