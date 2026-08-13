class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        gap = [0] * n

        t = 0
        for i in range(0,n):
            gap[i] = gas[i] - cost[i]
            t+=gap[i]

        if t < 0:
            return -1
        

        running_total = 0
        ans = 0
        i = 0

        while i < n:
            if running_total + gap[i] < 0:
                ans = (i+1)%n
                i = ans
                running_total = 0
                continue
            running_total += gap[i]
            i+=1
        return ans