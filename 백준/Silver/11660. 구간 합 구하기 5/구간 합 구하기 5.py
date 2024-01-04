import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
darr = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        darr[i][j] = darr[i - 1][j] + darr[i][j - 1] - darr[i - 1][j - 1] + arr[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(darr[x2-1][y2-1] - darr[x1-2][y2-1] - darr[x2-1][y1-2] + darr[x1-2][y1-2])