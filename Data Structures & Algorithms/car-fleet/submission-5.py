import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        time = []
        n = len(position)

        temp = []
        for i in range(0,n):
            temp.append((position[i],speed[i]))
        temp.sort()
            


        for i in range(0,n):
            info = temp[i]
            pos = info[0]
            sp = info[1]
            time_taken = (target - pos) / sp
            time.append(time_taken)



        for i in range(0,n):
            if not fleet:
                fleet.append(time[i])
                continue

            incoming_time = time[i]
            
            if fleet[-1] > incoming_time:
                fleet.append(incoming_time)
                continue

            while fleet and fleet[-1] <=incoming_time:
                # incoming is slow - so this stops other fast times
                fleet.pop()
            
                
            fleet.append(incoming_time)
        
        return len(fleet)
        
            
            
        
    

        