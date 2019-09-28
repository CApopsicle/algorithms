# 973. K Closest Points to Origin

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# distance of [1,3] is sqrt(10)
# distance of [-2, 2] is sqrt(8)

# [(distance, [x, y])]: min-heap: O(n), where n is number of points
# extract the smallest K times: Klogn

import heapq
def kClosest(points):
    '''
    input: list[list[int]]
    output: list[list[int]]
    '''
    queue = []
    ans = []
    for point in points:
        x, y = point
        heapq.heappush(queue, (x*x + y*y, point))
    for i in range(K):
        d, point = heapq.heappop(queue)
        ans.append(point)
    return ans

#Try Quick Select O(n) version
