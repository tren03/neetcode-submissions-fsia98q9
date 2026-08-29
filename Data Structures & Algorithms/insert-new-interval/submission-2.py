class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # we can add new interval to list
        # sort by first element
        # merge them
        ans = []
        i = 0
        # cur end smaller than new start
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # cur start <= new end
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1

        ans.append(newInterval)
        # remaining
        while i < len(intervals):
            ans.append(intervals[i])
            i+=1
        return ans
