n = int(input())
lst = list(map(int, input().split()))
V = 0
for i in range(n):
    if i == 0:
        V = lst[i]/100
    else:
        V = 1-(1-V)*(1-lst[i]/100)
    print(round(V*100, 6))