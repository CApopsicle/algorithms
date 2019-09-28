#621. Task Scheduler

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# You need to return the least number of intervals the CPU will 
# take to finish all the given tasks.

# AAABBBCCD, n = 3
# A???A???A
# AB??AB??AB


def taskScheduler1(tasks, n):
    '''
    input: list[char]
    output: int
    '''
    counter = [0] * 26
    for task in tasks:
        counter[ord(task) - ord('A')] += 1
    
    maxCount = max(counter)

    numOfMaxCount = 0
    for count in counter:
        if count == maxCount:
            numOfMaxCount += 1
    
    partCount = maxCount - 1
    emptySpot = partCount * (n - numOfMaxCount + 1)
    availableTask = len(tasks) - numOfMaxCount * maxCount
    idle = max(0, emptySpot - availableTask)
    # ["A","A","A","B","B","B"], 0 in this case, idle would be negative
    ans = len(tasks) + idle
    return ans

print(taskScheduler1(["A","A","A","B","B","B","C","C","D"], 3))
print(taskScheduler1(["A","A","A","B","B","B"], 2))

import heapq
import collections
def taskScheduler2(tasks, n):
    counter = collections.Counter(tasks)
    queue = []
    heapq.heapify(queue)
    for char, count in counter.items():
        heapq.heappush(queue, (-1 * count, char))
    #[(-3, A), (-3, B), (-2, C), (-1, D)]
    ans = 0
    while queue:
        #[(-1, A), (-1, B)]
        k = n + 1
        temp = []
        while k > 0 and queue:
            count, char = heapq.heappop(queue)
            temp.append((-1 * count, char))
            k -= 1
        
        ans += len(temp)
        for count, key in temp:
            if count - 1 > 0:
                heapq.heappush(queue, (-1*(count-1), char))
        if len(queue) == 0:
            break
        if k > 0:
            ans += k
    return ans

print(taskScheduler2(["A","A","A","B","B","B","C","C","D"], 3))
