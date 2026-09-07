"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        print(starts,ends)
        s = 0
        e = 0
        ans = 0
        count = 0
        while e < len(intervals):
            cur_end = ends[e]
            if s < len(intervals) and starts[s] < cur_end:
                count += 1
                s += 1
                ans = max(ans, count)
                continue
            count -= 1
            e += 1
        return ans



            
