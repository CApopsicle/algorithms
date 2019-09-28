#523. Continuous Subarray Sum

# Given a list of non-negative numbers and a target integer k, 
# write a function to check if the array has a continuous subarray of size
# at least 2 that sums up to *a multiple of k*, that is, 
# sums up to n*k where n is also an integer.

# Input: [23, 2, 4, 6, 7],  k=6
# Output: True

# Input: [23, 2, 6, 4, 7],  k=42
# Output: True

# set(5, 1, 29)
# 29 - 6 = 23

def checkSubarraySum(nums, k):
    numMap = {0: -1}
    accu = 0
    for i, num in enumerate(nums):
        accu += num
        mod = accu % k if k != 0 else accu
        if mod in numMap:
            #has a continuous subarray of size at least 2
            #we need to keep track of index, so we can't use Set
            if i - numMap[mod] > 1: 
                return True
        else:
            numMap[mod] = i
    return False

print(checkSubarraySum([23, 2, 4, 6, 7], 6), True)
print(checkSubarraySum([23, 2, 4, 6, 7], -6), True)
print(checkSubarraySum([23, 2, 6, 4, 7], 42), True)
print(checkSubarraySum([23, 2, 6, 4, 7], 0), False)
print(checkSubarraySum([0], 0), False)