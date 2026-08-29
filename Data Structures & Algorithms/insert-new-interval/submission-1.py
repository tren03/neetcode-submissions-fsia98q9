class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # we can add new interval to list
        # sort by first element
        # merge them

        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        i = 1
        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            if prev_end < cur_start:
                prev_end = cur_end
                prev_start = cur_start
                i += 1
                continue
            
            # merge intervals
            popped = intervals.pop(i)
            intervals[i-1][1] = max(prev_end,cur_end)
            prev_end = intervals[i-1][1]

        return intervals
        