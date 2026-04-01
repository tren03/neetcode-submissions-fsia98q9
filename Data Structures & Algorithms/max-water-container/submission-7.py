class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #to increase area, we can increase width, or height.
        # when we move the pointers, width decreases by default, so we will have
        # to increase the height - height = min(l,r)


        l = 0
        r = len(heights) -1
        
        answer = 0
        while(l<r):
            cur_area = min(heights[l],heights[r]) * (r-l)
            answer = max(answer,cur_area)
            

            # we decide to move l or r 
            # move the pointer that points to least val, as that is 
            # not of any use to us, we can check other vals
            if heights[l] < heights[r]:
                l=l+1
            else:
                r=r-1
            answer = max(answer,cur_area)
        return answer
            
            


        

            



        