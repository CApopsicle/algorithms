# 76. Minimum Window Substring

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

# Input: S = "ABAACBAB", T="ABC"
# Output: "ACB"

from collections import Counter

def minWindowSubstring(s, t):
    tMap = Counter(t)
    curMap = {}
    i, j = 0, 0
    count = 0
    ans = (float('inf'), 0, 0) # ans stores in the form of length, i, j
    while j < len(s):
        curMap[s[j]] = curMap.get(s[j], 0) + 1
        if s[j] in tMap and curMap[s[j]] == tMap[s[j]]:
            count += 1
        
        while count == len(tMap):
            if j - i + 1 < ans[0]:
                ans = (j - i + 1, i, j)

            curMap[s[i]] -= 1
            if curMap[s[i]] < tMap[s[i]]:
                count -= 1

            i += 1

        j += 1
    return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]

print(minWindowSubstring("ABAACBAB", "ABC"))
print(minWindowSubstring("ADOBECODEBANC", "ABC"))


