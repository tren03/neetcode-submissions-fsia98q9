class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        m = {}
        ans = 0

        while r < n:
            m[s[r]] = m.get(s[r],0) + 1

            max_freq = 0
            for key,v in m.items():
                max_freq = max(max_freq,v)


            while ((r-l+1) - max_freq) > k and l<r:
                to_remove = s[l]

                if m[to_remove] == 1:
                    del m[to_remove]
                else:
                    m[to_remove] -= 1

                l += 1

            # for sure valid here
            ans = max(ans, r-l+1)
            r += 1
        return ans


        
