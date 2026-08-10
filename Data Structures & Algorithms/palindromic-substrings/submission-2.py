class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = 0

        for i,char in enumerate(s):
            # each char is a palindrome
            ans += 1

            # odd case, start from i-1, i+1
            l = i-1
            r = i+1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                    continue
                break

            l = i
            r = i+1
            # even case, start from i, i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                    continue
                break
                
        return ans



            

        