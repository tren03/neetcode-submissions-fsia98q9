class Solution:
    def numDecodings(self, s: str) -> int:
        self.dp = [-1] * len(s)
        def rec(i):
            if i >= len(s):
                return 1
            if self.dp[i] != -1:
                return self.dp[i]
            if int(s[i]) == 0:
                return 0


            a = 0
            b = 0
            one = int(s[i])
            two = 0
            if i != len(s)-1:
                two = int(s[i:i+2])

            a = rec(i+1)
            if two <= 26 and two > 0:
                b = rec(i+2)
                
            self.dp[i] = a+b
            return a + b

        return rec(0)
                
                
                    
                





            
            