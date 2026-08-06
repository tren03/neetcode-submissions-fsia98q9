class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        m = set()
        ans = 0

        while r < len(s):
            char = s[r]
            if char not in m:
                m.add(char)
                r += 1
                ans = max(ans, len(m))
                continue
            
            # if exists:
            # pop until no dups
            while l <= r and char in m:
                m.remove(s[l])
                l += 1
            m.add(char)
            r += 1
        return ans
            

        