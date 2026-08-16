class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)


        def rec(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if dp[i] != -1:
                return dp[i]

            nos1 = s[i]
            nos2 = None
            if i < len(s) - 1:
                if int(s[i:i+2]) <= 26:
                    nos2 = int(s[i:i+2])
            
            # choose nos1
            n1 = rec(i+1)

            # choose nos2
            n2 = 0
            if nos2 is not None:
               n2 = rec(i+2)
            
            dp[i] = n1 + n2
            return dp[i]
            
        
        return rec(0)

            
            


        
            

        