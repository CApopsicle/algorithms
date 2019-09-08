#215. Kth Largest Element in an Array
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
import heapq
def findKthLargest1(nums, k):
    '''
    input: list[int], int
    output: int
    '''
    #Use heap(min-heap): O(k+(n-k)logk)
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for i in range(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

def findKthLargest2(nums, k):
    while len(nums) > 0:
        pivot = nums[0]
        left, right = [], []
        for i in range(1, len(num)):
            if nums[i] < pivot:
                left.append(nums[i])
            else: 
                right.append(nums[i])
        #len(right)+1 because pivot is considered as the right team
        if len(right)+1 > k:
            nums = right
        elif len(right)+1 < k:
            nums = left
            k -= len(right) + 1
        else:
            return pivot