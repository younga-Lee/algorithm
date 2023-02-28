T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) #배열의 세로, 가로
    arr = [input() for _ in range(N)]

    #암호를 찾아보자
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] != '0':
                word = arr[i][:j+1]
                break
    print(word)
    print(f'#{tc}')