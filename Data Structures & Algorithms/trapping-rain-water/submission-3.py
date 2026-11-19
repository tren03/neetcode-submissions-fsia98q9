class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        left_max = []
        right_max = []

        cur_max = height[0]
        for cur in height:
            cur_max = max(cur_max, cur)
            left_max.append(cur_max)

        cur_max = height[-1]
        height.reverse()
        for cur in height:
            cur_max = max(cur_max, cur)
            right_max.append(cur_max)
        right_max.reverse()



        for ind, cur in enumerate(height):
            cur_ans = 0
            left_tallest = left_max[ind]
            right_tallest = right_max[ind]

            area_held_above_cur = min(left_tallest, right_tallest) - cur


            ans += area_held_above_cur

        return ans








    