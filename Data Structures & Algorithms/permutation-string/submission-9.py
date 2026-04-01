class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
                
        s1_map = {}
        for i in s1:
            if i not in s1_map:
                s1_map[i] = 1
            else:
                s1_map[i] +=1
        
        s2_map = {}

        l,r=0,0
        while(r<len(s2)):
            print(s1_map,s2_map)
            if r < len(s1):
                # just add
                if s2[r] not in s2_map:
                    s2_map[s2[r]] = 1
                else:
                    s2_map[s2[r]] +=1
                r+=1
                continue

            #do checkVjj 
            if s1_map == s2_map:
                return True
            
            #pop l, add r
            if s2_map[s2[l]]==1 :
                del s2_map[s2[l]]
            else:
                s2_map[s2[l]] -=1
            l+=1

            if s2[r] not in s2_map:
                s2_map[s2[r]] = 1
            else:
                s2_map[s2[r]] +=1
            r+=1
            #do check 
            if s1_map == s2_map:
                return True
        if s1_map == s2_map:
            return True

        return False



