#350. Intersection of Two Arrays II

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# 1. Use HashMap
# Time Complexity: O(N + M), M is number of elements of num2
# Space Complexity: O(N), N is number of elements of nums1

# 2. Sort
# Time Complexity: O(NlogN, MlogM)
# Space Complexity: O(1)

from collections import Counter

def intersect1(nums1, nums2):
    dict1 = Counter(nums1)
    ans = []
    for num in nums2:
        if num in dict1:
            ans.append(num)
            dict1[num] -= 1
            if dict1[num] == 0:
                del dict1[num]
    return ans

print(intersect1([1,2,2,1], [2,2]))
print(intersect1([4,9,5], [9,4,9,8,4]))

def intersect2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    ans = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return ans

print(intersect2([1,2,2,1], [2,2]))
print(intersect2([4,9,5], [9,4,9,8,4]))

# 0xb7e57190
# 0xb7f77a24
# 0xb7e4a1e0
