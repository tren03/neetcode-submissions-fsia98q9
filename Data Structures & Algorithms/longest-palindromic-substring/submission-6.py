class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        logic is to start at and index.
        from that index, what is max lenght of palindromic string possible
        ababd
        for index i, assume that the index is the middle
        extend on both sides. but now, for even palindrome checking, 
        just start l/r from the index.
        dfs(i) would represt max length palindrom assuming that value is
        at the middle
        """

        ans = ""
        for i in range(len(s)):
            l = i-1
            r = i+1
            cur = s[i]
            if len(cur) > len(ans):
                ans = cur

            while l>=0 and r<len(s) and s[l] == s[r]:
                cur = s[l:r+1]
                if len(cur) > len(ans):
                    ans = cur
                l -= 1
                r += 1

            l = i
            r = i+1
            cur = s[i]
            if len(cur) > len(ans):
                ans = cur
            while l>=0 and r<len(s) and s[l] == s[r]:
                cur = s[l:r+1]
                if len(cur) > len(ans):
                    ans = cur
                l -= 1
                r += 1
        return ans


        