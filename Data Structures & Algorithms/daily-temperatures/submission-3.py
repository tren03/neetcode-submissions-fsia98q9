class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = []
        for i in range(len(temperatures)-1,-1,-1):
            if len(st) == 0:
                ans.append(0)
                st.append(i)
                continue
            # stack has some values.
            # as an element, i only care about
            # values greater than myself.
            # so i want to remove all smaller elements 
            # till i reach an element greater than myself, or nil stack

            cur = temperatures[i]
            while len(st) and temperatures[st[-1]] <= cur:
                st.pop()
            
            # we did not find any elements that are greater than me
            if not len(st):
                ans.append(0)
            else:
                diff = st[-1] - i
                ans.append(diff)

            st.append(i)
        
        ans.reverse()
        return ans



        