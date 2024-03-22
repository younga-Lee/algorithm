n = int(input())
lst = list(map(int, input().split()))
od = 1 #순서
stk = []
snack = []
ans = 'Nice'

i = 0
while i != n:
    if lst[i] == od:
        snack.append(lst[i])
        od += 1
        i += 1
    else:
        if stk:
            if stk[-1] == od:
                snack.append(stk.pop())
                od += 1
            else:
                stk.append(lst[i])
                i += 1
        else:
            stk.append(lst[i])
            i += 1
while stk:
    if snack[-1]+1 != stk[-1]:
        ans = 'Sad'
        break
    else:
        snack.append(stk.pop())

print(ans)