n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(n):
    arr[i+1] += arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(arr[b]-arr[a-1])