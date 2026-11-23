class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        ans = 0
        m = defaultdict(int)

        def max_occ(m):
            mx = 0
            for val in m.values():
                mx = max(val,mx)
            return mx

        while r < len(s):
            m[s[r]] += 1
            mx = max_occ(m)
            valid_window = ((r-l)+1) <= (mx + k)
            if valid_window:
                ans = max((r-l)+1, ans)
            else:
                #print("not valid", l,r,m[s[r]], s[r],((r-l)+1),(mx + k),m )
                while not valid_window and l<r:
                    val_to_remove = s[l]
                    if m[val_to_remove] == 1:
                        del m[val_to_remove]
                    else:
                        m[val_to_remove]-=1
                    l+=1
                    mx = max_occ(m)
                    valid_window = ((r-l)+1) <= (mx + k)
            r+=1
        return ans











        