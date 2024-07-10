class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 1
        
        minRooms, endPtr = 0, 0

        startTimes = [intervals[i][0] for i in range(len(intervals))]
        endTimes = [intervals[i][1] for i in range(len(intervals))]
        startTimes.sort()
        endTimes.sort()

        for i in range(0, len(startTimes)):
            if startTimes[i] >= endTimes[endPtr]: endPtr += 1
            else: minRooms += 1

        return minRooms