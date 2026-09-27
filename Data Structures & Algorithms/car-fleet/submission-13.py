class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        d = []
        for i in range(len(position)):
            d.append((position[i], speed[i]))
        d.sort()

        times = []
        for v in range(len(d)):
            dist = target - d[v][0]
            speed = d[v][1]
            times.append(dist/speed)

        for i in range(len(times)-1, -1, -1):
            t = times[i]
            if not len(st):
                st.append(t)
                continue
            
            if t > st[-1]:
                st.append(t)


        return len(st)




        