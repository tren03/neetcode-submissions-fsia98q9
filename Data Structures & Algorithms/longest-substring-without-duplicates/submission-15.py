class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()

        l = 0
        r = 0
        ans = 0
        n = len(s)

        while r < n:
            val = s[r]
            if val not in m:
                m.add(val)
                ans = max(ans, r-l+1)
                r += 1
                continue
        
            # issue is shortening the window
            # we have a value that is in m
            while l<r and s[l] != val:
                m.remove(s[l])
                l += 1
            l += 1
            r += 1

        return ans

