#953. Verifying an Alien Dictionary

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false

# turn order into a dictionary
# for every pair of words, compare every char from the start
# if not sort return False
# once finish the for loop return True

# Time complexity: O(N), N is the number of words
# Space complexity: O(1), 26 alphebets in dictionary

def isAlienSorted(words, order):
    '''
    input: list[string], string
    output: bool
    '''
    wordDic = {char: i for i, char in enumerate(order)}
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        #deal with "apple" and "app" condition
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return False
        for char1, char2 in zip(word1, word2):
            if wordDic[char1] > wordDic[char2]:
                return False
            elif wordDic[char1] < wordDic[char2]:
                break
    return True

print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))