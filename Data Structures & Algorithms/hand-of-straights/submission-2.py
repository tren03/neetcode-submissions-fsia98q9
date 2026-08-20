class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        m = {}
        for i in hand:
            m[i] = m.get(i,0) + 1
        
        for i in hand:
            if m[i] == 0:
                continue
            # find group from i
            temp = 0 # include i 
            val = i
            while temp < groupSize:
                if val not in m or m[val] == 0:
                    return False
                m[val] -= 1
                temp += 1
                val = val+1

        return True


        