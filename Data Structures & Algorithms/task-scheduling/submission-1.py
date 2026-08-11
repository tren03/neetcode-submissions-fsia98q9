class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        m = {}

        for i in tasks:
            m[i] = m.get(i,0) + 1
        
        mheap = []
        for key,freq in m.items():
            heapq.heappush(mheap,(-freq,key)) #(freq,key)

        q = [] #(key,freq,next_time_available)

        while q or mheap:
            # populate mheap from q if elements present
            while q and q[0][2] == t:
                popped = q[0]
                q = q[1:]
                heapq.heappush(mheap,(popped[1],popped[0]))

            # process one element
            if mheap:
                popped = heapq.heappop(mheap)
                key = popped[1]
                freq = popped[0]

                if freq != -1:
                    q.append((key,freq+1,t+n+1))
            t += 1
        
        return t
        