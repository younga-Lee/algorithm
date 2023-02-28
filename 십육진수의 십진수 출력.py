def Bbit_print(i):
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1 << j) else '0'
    return output

T = int(input())
for tc in range(1, T + 1):
    num = input()

    #16진법 -> 2진법
    arr = ''
    for n in num:
        if n.isdigit():
            t = ord(n) - ord('0')
            arr += Bbit_print(t)
        else:
            t = ord(n)-ord('A')+10
            arr += Bbit_print(t)

    #2진법 -> 10진법
    ans = []
    for i in range(0, len(arr),7):
        ans.append(str(int(arr[i:i+7],2)))
    print(f'#{tc}', *ans)