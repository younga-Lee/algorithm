a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))
ans = 0
ans += len(a_set-b_set)
ans += len(b_set-a_set)
print(ans)