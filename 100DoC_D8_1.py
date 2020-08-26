def longestMountain(A):
    longest = 0
    for i in range(1, len(A) - 1):
        if A[i-1] < A[i] > A[i+1]:
            i_l, i_r = i-2, i+2
            while i_l > -1 and A[i_l] < A[i_l + 1]: i_l -= 1
            while i_r < len(A) and A[i_r] < A[i_r - 1]: i_r += 1
            longest = max(i_r - i_l - 1, longest)
            i = i_r
        else: i += 1
    return longest
A=[2,2,2]
print(longestMountain(A))
