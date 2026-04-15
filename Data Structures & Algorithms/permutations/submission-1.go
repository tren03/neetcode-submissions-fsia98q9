func permute(nums []int) [][]int {
    var r func([]int,int)
    ans := make([][]int, 0)

    r = func(temp []int,ind int){
        if ind >= len(nums){
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }
        for i := ind; i < len(nums); i++{
            // swap ind and i index
            temp[ind], temp[i] = temp[i], temp[ind]
            r(temp, ind+1)
            temp[i], temp[ind] = temp[ind], temp[i]
        }
    }
    r(nums, 0)
    return ans
    
}