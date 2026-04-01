class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        ans = 0
        hmap = {}
        while(r < len(s)):
            if s[r] not in hmap:
                hmap[s[r]] = r
                ans = max(len(hmap),ans)
                r+=1
            else:
                while(1):
                    if s[l] == s[r]:
                        hmap.pop(s[l])
                        l+=1
                        break
                    else:
                        hmap.pop(s[l])
                    l+=1
                hmap[s[r]] = r
                r+=1
            print(hmap)
                
            

            
        return ans
        