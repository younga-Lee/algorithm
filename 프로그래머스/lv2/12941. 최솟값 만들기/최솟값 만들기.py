def solution(A,B):
    total = 0
    A = sorted(A)
    B = sorted(B, reverse = True)
    for i in range(len(A)):
        total += A[i]*B[i]
    return total