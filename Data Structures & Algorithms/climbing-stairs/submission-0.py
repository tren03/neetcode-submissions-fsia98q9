class Solution:
    def climbStairs(self, n: int) -> int:

        def f(i):
            if i <= 1:
                return 1
            l = f(i-1)
            r = f(i-2)
            return l+r
        ans = f(n)
        return ans
                

        