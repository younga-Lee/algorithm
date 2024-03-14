n = int(input())
arr = [[0]*n for _ in range(n)]
ans = 0 #답 (시간)
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 2 #사과가 있다면 2

l = int(input())
dr = [(0, 1), (1, 0), (0, -1), (-1, 0)] #방향 : 오른 아래, 왼, 위
l_lst = []
for _ in range(l):
    t, d = input().split()
    l_lst.append((int(t), d))

#뱀의 위치 ~ 1로 설정
r = 0 #오른쪽방향부터 시작
i, j = 0, 0
snake = [(i, j)]
arr[i][j] = 1
while snake:
    i, j = snake[-1]
    ans += 1

    #뱀의 이동
    ni, nj = i+dr[r][0], j+dr[r][1]

    if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 1:
        break #종료조건 : 벽에 부딪히거나 자기 몸에 부딪힐 경우

    if arr[ni][nj] != 2: #사과를 없다면
        a, b = snake.pop(0)
        arr[a][b] = 0
    arr[ni][nj] = 1
    snake.append((ni, nj))

    # 방향 전환
    if l_lst and ans == l_lst[0][0]:  # 시간
        t, d = l_lst.pop(0)
        if d == 'L':
            r = (r - 1) % 4
        else:
            r = (r + 1) % 4
print(ans)