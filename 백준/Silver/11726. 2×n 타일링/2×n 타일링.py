import sys
input = sys.stdin.readline

n = int(input())
ans = 0

if n == 1:
    print(1%10007)
    exit()
lst = [0]*(n+1)
lst[1] = 1
lst[2] = 2

#규칙성: 피보나치
for i in range(3, n+1):
    lst[i] = lst[i-2] + lst[i-1]
print(lst[n]%10007)

