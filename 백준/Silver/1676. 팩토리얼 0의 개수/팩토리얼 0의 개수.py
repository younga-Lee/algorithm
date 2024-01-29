n = int(input())
num = 1
for i in range(n, 1, -1):
    num *= i

ans = 0
for j in range(len(str(num))-1, 0, -1):
    if str(num)[j] == '0':
        ans += 1
    else:
        break
print(ans)