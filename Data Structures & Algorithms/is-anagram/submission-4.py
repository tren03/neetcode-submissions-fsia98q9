class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}

        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        
        for i in t:
            if i not in m:
                return False
            if m[i] == 1:
                del m[i]
            else:
                m[i] -= 1

        if not m:
            return True
        return False

        