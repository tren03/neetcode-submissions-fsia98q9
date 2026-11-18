class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        cur = 0

        while l < r:
            breadth = r-l
            if heights[l] < heights[r]:
                ans = max(ans, heights[l] * breadth)
                l += 1
            else:
                ans = max(ans, heights[r] * breadth)
                r -= 1
    
        return ans




        