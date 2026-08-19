class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        w = wordDict
        m = set()
        for i in w:
            m.add(i)
        dp = [0] * len(s)

        def rec(i):
            if i == len(s):
                return True
            if isinstance(dp[i],bool):
                return dp[i]

            pref = ""
            for j in range(i,len(s)):
                pref += s[j]
                if pref in m:
                    ans = rec(j+1)
                    if ans:
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return rec(0)


        