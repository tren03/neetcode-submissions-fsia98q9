class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        ans = 0
        m = set()

        while r < len(s):
            if s[r] not in m:
                ans = max(ans, (r-l)+1)
                m.add(s[r])
                r += 1
                continue
            
            while s[l] != s[r] and l < r:
                m.remove(s[l])
                l+=1
            l+=1
            m.add(s[r])

            r += 1

        return ans

        
        