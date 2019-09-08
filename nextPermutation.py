# 31. Next Permutation
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# The replacement must be **in-place** and use only constant extra memory.

# search from the right of input array, and find the increasing part
# save the key of increasing part 
# find the next number just bigger than nums[key] from the right of the array
# because the right part is a drcreasing array
# switch them and reverse the right part

#Time complexity: O(N), N is the number of input

def nextPermutation(nums):
    '''
    input: list[int]
    output: list[int]
    '''
    n = len(nums)
    key = -1
    for i in range(n-1, -1, -1):
        if nums[i-1] < nums[i]:
            key = i-1
            break
    
    if key == -1:
        #This is a total decreasing array, 3,2,1 → 1,2,3 reverse it
        i, j = 0, n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    else:
        #find the next number just bigger than nums[key]
        for j in range(n-1, -1, -1):
            if nums[j] > nums[key]:
                #swap nums[key] and nums[j]
                nums[key], nums[j] = nums[j], nums[key]
                break
        #reverse nums[key+1:]
        i, j = key+1, n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1