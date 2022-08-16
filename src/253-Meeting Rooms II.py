class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # minimum number of meeting room = Max number of meeting that need to run in paralle
        # first split meeting into start and end

        starts = []
        ends = []
        for s, e in intervals:
            starts.append(s)
            ends.append(e)
        starts.sort()
        ends.sort()
        max_room = 0
        e = 0
        for s in range(len(starts)):
            if starts[s] < ends[e]:
                max_room += 1
            else:
                e += 1  # check next ending time if current start time is later then current end
        return max_room
