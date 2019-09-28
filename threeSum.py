#15. 3Sum

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def threeSum(nums):
    '''
    input: list[int]
    '''
    nums.sort()
    i = 0
    res = []
    # len(nums)-2 is because we need at least 3 numbers to continue
    for i in range(len(nums) - 2):
        # Below if because we don't need to check duplicate targets
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = 0 - nums[i]
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
    return res

print(threeSum([-1, 0, 1, 2, -1, -4]))
