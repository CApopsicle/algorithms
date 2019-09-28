# 67. Add Binary

# Input: a = "11", b = "1"
# Output: "100"

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):
    '''
    input: str, str
    output: str
    '''
    ans = ""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    while i >= 0 or j >= 0:
        if i >= 0:
            carry += int(a[i])
        if j >= 0:
            carry += int(b[j])

        # Below can be replace into
        # ans += str(carry % 2)
        # carry = carry // 2
        if carry == 0:
            ans += str(carry)
        elif carry == 1:
            ans += str(carry)
            carry = 0
        elif carry == 2:
            ans += "0"
            carry = 1
        elif carry == 3:
            ans += "1"
            carry = 1

        i -= 1
        j -= 1

    if carry:
        ans += str(carry)
    return ans [::-1]

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
