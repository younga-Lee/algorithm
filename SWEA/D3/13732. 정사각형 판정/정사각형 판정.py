def check(arr):
    global ans
    for a in range(si, ei+1):
        for b in range(sj, ej+1):
            if arr[a][b] == '.':
                ans = 'no'
                return False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'yes'

    flag1, flag2 = False, False
    si, sj = -1, -1
    ei, ej = -1, -1

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                si, sj = i, j
                flag1 = True
                break
        if flag1 == True:
            break
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j] == '#':
                ei, ej = i, j
                flag2 = True
                break
        if flag2 == True:
            break
    check(arr)
    if si < 0 or sj < 0 or ei < 0 or ej < 0 or ei-si != ej-sj:
        ans = 'no'
    print(f'#{tc} {ans}')