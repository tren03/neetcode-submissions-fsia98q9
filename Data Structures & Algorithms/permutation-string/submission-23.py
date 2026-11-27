class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = defaultdict(int)
        for val in s1:
            m1[val] += 1

        l,r = 0,0

        m2 = defaultdict(int)
        while r < len(s2):
            cur = s2[r]
            if r < len(s1):
                m2[cur] += 1
                if m2 == m1:
                    return True
                r+=1
                continue
            
            m2[cur] += 1
            to_remove = s2[l]
            print(l,r, to_remove)
            if m2[to_remove] > 1:
                m2[to_remove] -= 1
            else:
                del m2[to_remove]
            l+=1
            r+=1
            print(m2, m1)

            if m2 == m1:
                return True
    
        return False

        



        