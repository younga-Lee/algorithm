N, K = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr[:K])
mx = total
for i in range(1, N-K+1):
    total = total - arr[i-1]+arr[i+K-1]
    if total > mx:
        mx = total
print(mx)