class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wd = set()
        for i in wordDict:
            wd.add(i)

        dp = {}

        def dfs(i,sub):
            if i >= len(s) and sub == "":
                return True
            if i >= len(s):
                return False
            if dp.get((i,sub)) is not None:
                return dp[(i,sub)]

            cur = s[i]
            temp = sub+s[i]
            if temp in wd:
                a = dfs(i+1,temp)
                b = dfs(i+1,"")
                dp[(i,sub)] = a or b
                return a or b
            else:
                c =  dfs(i+1,temp)
                dp[(i,sub)] = c
                return c
                
        return dfs(0,"")

        

        