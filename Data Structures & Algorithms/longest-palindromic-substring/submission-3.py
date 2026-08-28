class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for ind,i in enumerate(s):
            # assume ind is center
            temp = i
            l = ind-1
            r = ind+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    temp = s[l] + temp + s[r]
                    l-=1
                    r+=1
                else:
                    break
            if len(ans) < len(temp):
                ans = temp
            l = ind
            r = ind+1
            temp = ""
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    temp = s[l] + temp + s[r]
                    l-=1
                    r+=1
                else:
                    break
            if len(ans) < len(temp):
                ans = temp
        return ans

        