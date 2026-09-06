class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        ans = 0
        if len(intervals) == 1:
            return 0
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            # if not overlap, continue
            if prev_end <= start:
                prev_start = start
                prev_end = end
                continue
            
            # for overlap = we need to remove 1
            prev_start = min(start,prev_start)
            prev_end = min(end,prev_end)
            ans += 1
        
        return ans
            
        
        