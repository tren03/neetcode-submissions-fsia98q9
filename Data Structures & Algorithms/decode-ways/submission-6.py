class Solution:
    def numDecodings(self, s: str) -> int:
        a = 1 # represents dp[len(s)]
        b = 0 # represents dp[len(s)+1] - this is 0 as out of bounds

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                b = a
                a = 0
                continue
            cur_ans = 0
            # choose cur (a)
            cur_ans += a
            # choose nxt
            if i+2 <= len(s):
                if int(s[i:i+2]) <= 26:
                    cur_ans += b
            b = a
            a = cur_ans
        return a
            
        