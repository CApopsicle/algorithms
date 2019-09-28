#438. Find All Anagrams in a String

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

import collections

def findAnagrams(s, p):
    pCounter = collections.Counter(p)
    sCounter = collections.Counter(s[:len(p)-1])

    ans = []
    for i in range(len(p)-1, len(s)):
        sCounter[s[i]] = sCounter.get(s[i], 0) + 1

        head = i - (len(p) - 1)
        if sCounter == pCounter:
            ans.append(head)

        if sCounter[s[head]] > 1:
            sCounter[s[head]] -= 1
        else:
            del sCounter[s[head]]

    return ans

print(findAnagrams("cbaebabacd", "abc"))
