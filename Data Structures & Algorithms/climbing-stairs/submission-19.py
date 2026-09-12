class Solution:
    def climbStairs(self, n: int) -> int:
        # space optimized
        if n == 1:
            return 1
        a = 1
        b = 1
        for i in range(n-2,-1,-1):
            cur = a+b
            b = a
            a = cur
        return a
            




        