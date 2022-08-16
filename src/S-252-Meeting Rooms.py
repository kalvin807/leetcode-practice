class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            # Every meeting's endtime cannot later than next meeting start time
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
