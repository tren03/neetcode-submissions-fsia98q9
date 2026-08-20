class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mheap = []
        m = {}

        for i in hand:
            heapq.heappush(mheap,i)
            m[i] = m.get(i,0) + 1

        while mheap:
            lowest = mheap[0]
            heapq.heappop(mheap)
            if m[lowest] == 0:
                continue
            temp = 0
            while temp < groupSize:
                if lowest not in m or m[lowest] == 0:
                    return False
                m[lowest] -= 1
                temp += 1
                lowest = lowest + 1
            
        return True


        