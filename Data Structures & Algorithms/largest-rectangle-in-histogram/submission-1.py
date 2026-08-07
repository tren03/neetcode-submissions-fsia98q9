class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0

        for ind,h in enumerate(heights):
            if not st:
                st.append(ind)
                continue
            
            # if we get smaller element, we have found boundary 
            # for all ele in stack that is smaller than incoming
            while st and heights[st[-1]]>h:
                popped = st.pop()
                l = -1 if not st else st[-1]
                r = ind
                w = (r-l)-1
                ans = max(ans,w*heights[popped])
            
            st.append(ind)
        while st:
            popped = st.pop()
            l = -1 if not st else st[-1]
            r = len(heights)
            w = (r-l)-1
            ans = max(ans,w*heights[popped])

        return ans
            

        