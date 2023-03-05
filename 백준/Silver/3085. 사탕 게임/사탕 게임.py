N = int(input())
arr = [list(input()) for _ in range(N)]

#개수 확인
def check(arr):
    mx = 0
    arr2 = list(zip(*arr))
    for a in range(N):
        cnt = 1
        for b in range(1, N):
            if arr[a][b-1] == arr[a][b]: #한줄에 연속된다면
                cnt += 1
                if b == N-1:
                    if mx < cnt:
                        mx = cnt
                    cnt = 1
            else:
                if mx < cnt:
                    mx = cnt
                cnt = 1

    for a in range(N):
        cnt = 1
        for b in range(1, N):
            if arr2[a][b-1] == arr2[a][b]: #한줄에 연속된다면
                cnt += 1
                if b == N-1:
                    if mx < cnt:
                        mx = cnt
                    cnt = 1
            else:
                if mx < cnt:
                    mx = cnt
                cnt = 1

    return mx

#인접한 두칸 고르기
ans = 0
for i in range(N):
    for j in range(1, N):
        if arr[i][j-1] != arr[i][j]:
            arr[i][j-1], arr[i][j] = arr[i][j], arr[i][j-1]
            if ans < check(arr):
                ans = check(arr)
            arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1] #원상복구

for j in range(N):
    for i in range(1, N):
        if arr[i-1][j] != arr[i][j]:
            arr[i-1][j], arr[i][j] = arr[i][j], arr[i-1][j]
            if ans < check(arr):
                ans = check(arr)
            arr[i-1][j], arr[i][j] = arr[i][j], arr[i-1][j]
print(ans)