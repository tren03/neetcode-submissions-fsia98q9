func permute(nums []int) [][]int {
    var rec func([]int, int)

    ans := make([][]int, 0)

    rec = func(temp[]int, i int){
        fmt.Println(temp, i)
        if i == len(nums){
            t := make([]int, len(temp))
            copy(t, temp)
            ans = append(ans, t)
            return
        }

        // swap i with [i, (len(nums)-1)] 
        for j:=i;j<len(nums);j+=1{
            temp[i], temp[j] = temp[j], temp[i]
            rec(temp, i+1)
            temp[i], temp[j] = temp[j], temp[i]
        }
    }
    rec(nums,0)
    return ans

}
