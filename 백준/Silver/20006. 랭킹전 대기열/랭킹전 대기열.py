
p, m = map(int, input().split()) #플레이어 수, 방의 정원
ans = []
for _ in range(p):
    l, n = input().split() #레벨, 플레이어
    if not ans:
        ans.append([[int(l), n]])
    else:
        for i in range(len(ans)):
            if len(ans[i]) != m and (ans[i][0][0]-10<= int(l) <= ans[i][0][0]+10):
                ans[i].append([int(l), n])
                break
        else:
            ans.append([[int(l), n]])

for i in range(len(ans)):
    if len(ans[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    s_lst = sorted(ans[i], key=lambda x: x[1])
    for j in range(len(s_lst)):
        print(*s_lst[j])