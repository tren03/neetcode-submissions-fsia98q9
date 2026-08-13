class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        ans = 0

        while l < r:
            if heights[l] < heights[r]:
                m = l
            else:
                m = r

            area = (r-l) * heights[m]
            ans = max(area, ans)

            if m == l:
                l += 1
            else:
                r -= 1

        return ans

            
            


        