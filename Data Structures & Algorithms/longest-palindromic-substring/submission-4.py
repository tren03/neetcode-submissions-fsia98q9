class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_ans = 0
        r_ans = 0
        for ind,i in enumerate(s):
            # assume ind is center
            l = ind-1
            r = ind+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r_ans - l_ans < r-l:
                        l_ans = l
                        r_ans = r
                    l-=1
                    r+=1
                else:
                    break
            l = ind
            r = ind+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r_ans - l_ans < r-l:
                        l_ans = l
                        r_ans = r
                    l-=1
                    r+=1
                else:
                    break
        return s[l_ans:r_ans+1]

        