import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    exit()
lst = [0]*(n+1)
lst[0] = 1
lst[1] = 1

#규칙성: 피보나치
for i in range(2, n+1):
    lst[i] = (lst[i-2]*2 + lst[i-1])%10007
print(lst[n])
