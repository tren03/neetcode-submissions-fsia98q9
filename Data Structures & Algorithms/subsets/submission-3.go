import "slices"
func subsets(nums []int) [][]int {
    ans := make([][]int,0)
    var f func(a []int, index int)

    f = func(a []int, index int){
        fmt.Println(a,index)
        if index == len(nums){
            temp := make([]int, len(a))
            fmt.Println("here")
            copy(temp, a)
            ans = append(ans, temp)
            return
        }
        a = append(a, nums[index])
        f(a, index+1)
        a = slices.Delete(a, len(a)-1, len(a))    
        f(a, index+1)
    }

    a := make([]int, 0)
    index := 0

    f(a, index)
    return ans
}