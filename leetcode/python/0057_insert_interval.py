class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]

        # if newInterval comes before all intervals, insert it in the beginning
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        # append all previous intervals
        i, res = 0, []
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                res.append([intervals[i][0], intervals[i][1]])
                i += 1
            else: break

        # merge overlapping intervals
        start, end = newInterval[0], newInterval[1]
        while i < len(intervals):
            if end >= intervals[i][0]:
                start = min(start, intervals[i][0])
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            i += 1
        
        res.append([start, end])

        # append remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res