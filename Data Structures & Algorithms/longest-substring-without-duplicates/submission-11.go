func lengthOfLongestSubstring(s string) int {
    ans := 0
    l := 0
    r := 0
    m := make(map[byte]bool)
    
    for r < len(s){
        cur := s[r]
        _, ok := m[cur]
        if !ok{
            fmt.Println(l,r, s[l:r],cur, "not there")
            m[cur] = false
            ans = max(ans, (r-l)+1)
            r += 1
            continue
        }
        for l < r && s[l] != cur{
            fmt.Println(l,r, s[l:r],cur)
            delete(m, s[l])
            l += 1
        }
        delete(m, s[l])
        l += 1
        m[cur] = false
        r += 1
    }
    return ans

    
    
}