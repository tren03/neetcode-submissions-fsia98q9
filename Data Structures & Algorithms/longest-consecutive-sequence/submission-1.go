func longestConsecutive(nums []int) int {
    m := make(map[int]int)
    if len(nums) == 0{
        return 0
    }

    for _, v := range nums{
        m[v] += 1
    }

    ans := 1

    for _, v := range nums{
        if _, ok := m[v-1]; ok{
            continue
        }

        t := 1
        for i:= v+1;;i++{
            if _, ok := m[i]; ok{
                t += 1
                ans = max(ans, t)
                continue
            }
            break
        }
        
    }
    return ans

}
