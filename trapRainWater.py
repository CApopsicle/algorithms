# 42. Trapping Rain Water
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# Stack approach
# Time Complexity: O(N), single iteration
# Space Complexity: O(N), for stack, 
# and it takes up to O(N) space in case of stair-like or flat structure
def trapRainWater1(height):
    stack = []
    i, ans = 0, 0
    while i < len(height):
        if len(stack) == 0 or height[i] <= height[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            curLowLevel = stack.pop()
            if len(stack) == 0:
                tempWater = 0
            else:
                tempWater = (min(height[i], height[stack[-1]]) - height[curLowLevel]) * (i - stack[-1] - 1)
            ans += tempWater
    return ans
print(trapRainWater1([0,1,0,2,1,0,1,3,2,1,2,1]))

#Two pointer approach
#Time Complexity: O(N)
#Space Complexity: O(1)
def trapRainWater2(height):
    ans = 0
    left, right = 0, len(height) - 1 #index
    maxLeft, maxRight = 0, 0 #value
    while left < right:
        if height[left] <= height[right]:
            if height[left] < maxLeft:
                ans += maxLeft - height[left]
            else:
                maxLeft = height[left]
            left += 1
        else:
            if height[right] < maxRight:
                ans += maxRight - height[right]
            else:
                maxRight = height[right]
            right -= 1

    return ans

print(trapRainWater2([0,1,0,2,1,0,1,3,2,1,2,1]))