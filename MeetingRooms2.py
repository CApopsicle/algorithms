# 253. Meeting Rooms II

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

#sort input: nlogn
#keep track of endTime: priority queue:
#worst of N add operation and N extract-min operation
#extract-min is logn

import heapq
def meetingRooms2(intervals):
    '''
    input: list[list[int]]
    output: int
    '''
    intervals.sort(key = lambda x: x[0])
    q = []
    heapq.heapify(q)
    ans = 0
    for interval in intervals:
        if len(q) == 0 or interval[0] < q[0]:
            ans += 1
        else:
            heapq.heappop(q)
        heapq.heappush(q, interval[1])
    return ans

print(meetingRooms2([[0, 30],[5, 10],[15, 20]]))