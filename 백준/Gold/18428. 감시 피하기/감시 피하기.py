
n = int(input())
arr = [list(input().split()) for _ in range(n)]
ans = 'NO'
# 선생님 위치 구하기
t = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            t.append((i, j))

# 선생님들이 감시
def check():
    dr = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for ti, tj in t:
        for di, dj in dr:
            ni, nj = ti + di, tj + dj
            while True:
                if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj] == 'O':
                    break
                if arr[ni][nj] == 'S':
                    return False  # 학생 딱 걸림
                ni += di
                nj += dj
    return True

# 장애물 설치하기
def dfs(cnt):
    global ans
    if cnt == 3:
        if check() is True:
            ans = 'YES'
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                dfs(cnt + 1)
                arr[i][j] = 'X'

dfs(0)
print(ans)

