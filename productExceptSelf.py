#238. Product of Array Except Self
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

#construct 2 array: L and R
#Time complexity: O(n), Space complexity: O(n)
#L:[1,1,2,6]
#R:[24,12,4,1]
def productExceptSelf1(nums):
    '''
    input: list[int]
    output: list[int]
    '''
    n = len(nums)
    L, R, ans = [0] * n, [0] * n, [0] * n
    L[0] = 1
    R[n-1] = 1
    
    for i in range(1, n):
        L[i] = L[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        R[i] = R[i+1] * nums[i+1]
    
    for i in range(n):
        ans[i] = R[i] * L[i]
    
    return ans

def productExceptSelf2(nums):
    #O(1) space approach
    #construct ans array like L
    #use single variable R to keep track of the running product
    n = len(nums)
    ans = [0] * n
    ans[0] = 1
    for i in range(1, n):
        ans[i] = ans[i-1] * nums[i-1]
    
    R = 1
    for i in range(n-1, -1, -1):
        ans[i] = ans[i] * R
        R = R * nums[i]
    return ans