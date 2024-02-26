def solution(n, m):
    ans = 0
    for i in range(1, max(n, m)+1):
        if n%i == 0 and m%i == 0:
            ans = i
    ans2 = n*m//ans
    return ans, ans2