class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        if len(intervals) == 0:
            return [[]]
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        i = 1
        while i < len(intervals):
            cur = intervals[i]
            cur_start = cur[0]
            cur_end = cur[1]

            print(cur_start,prev_end)
            if cur_start > prev_end:
                prev_start = cur_start
                prev_end = cur_end
                i += 1
                continue
            
            # conflict - merge cur and prev (dont increment i)
            new_start = prev_start
            new_end = cur_end
            intervals.pop(i)
            intervals[i-1][0] = prev_start
            intervals[i-1][1] = max(cur_end, prev_end)
            prev_end = max(cur_end, prev_end)
        
        return intervals





        
        