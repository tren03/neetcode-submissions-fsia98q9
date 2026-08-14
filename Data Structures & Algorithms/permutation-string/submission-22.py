class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = {}
        m2 = {}

        for i in s1:
            m1[i] = m1.get(i,0) + 1

        l = 0
        r = 0

        while r < len(s2):
            if r < len(s1):
                m2[s2[r]] = m2.get(s2[r],0) + 1
                r += 1
                continue
            
            if m1 == m2:
                return True
            
            # add r
            m2[s2[r]] = m2.get(s2[r],0) + 1
            # remove l
            if m2[s2[l]] == 1:
                del m2[s2[l]]
            else:
                m2[s2[l]] -= 1

            if m1 == m2:
                return True
            r += 1
            l += 1
            
        if m1 == m2:
            return True

        return False
        




        