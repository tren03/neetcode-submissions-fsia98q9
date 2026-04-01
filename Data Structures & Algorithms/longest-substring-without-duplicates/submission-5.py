class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        l = 0
        r = 0
        answer = 0

        while r<len(s):
            print(l,r)
            if s[r] not in s_set:
                s_set.add(s[r])
                answer = max(len(s_set),answer)
            else:
                print(s[l],s[r])
                while s[l] != s[r]:
                    s_set.remove(s[l])
                    l+=1
                s_set.remove(s[l])
                l+=1
                s_set.add(s[r])
            r+=1
        return answer

        