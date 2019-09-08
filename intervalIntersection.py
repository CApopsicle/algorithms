#986. Interval List Intersections

# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# O(M+N) approach: M is the length of A, and N is the length of B

def intervalIntersection(A, B):
    '''
    input: list[list[int]], list[list[int]]
    output: list[list[int]]
    '''
    i, j = 0, 0
    ans = []
    while i < len(A) and j < len(B):
        maxStart = max(A[i][0], B[j][0])
        minEnd = min(A[i][1], B[j][1])

        if maxStart <= minEnd:
            ans.append([maxStart, minEnd])

        if A[i][1] < B[j][1]:
            i += 1
        elif B[j][1] < A[i][1]:
            j += 1
        else:
            i += 1
            j += 1
    return ans