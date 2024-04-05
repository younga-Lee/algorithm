from collections import deque

# 입력 처리
tc = int(input())
for _ in range(tc):
    w, h = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]

    fire_q = deque()
    sanggeun_q = deque()

    # 초기 위치 설정
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                sanggeun_q.append((i, j, 0))  # 상근이 위치와 시간
            elif arr[i][j] == '*':
                fire_q.append((i, j))  # 불 위치

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # 불 확산 함수
    def fire():
        len_q = len(fire_q)
        for _ in range(len_q):
            x, y = fire_q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '#' and arr[nx][ny] != '*':
                    arr[nx][ny] = '*'
                    fire_q.append((nx, ny))

    # 상근이 이동 함수
    def move():
        len_sq = len(sanggeun_q)
        for _ in range(len_sq):
            x, y, time = sanggeun_q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return time + 1  # 탈출 성공
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '@'  # 상근이 이동
                    sanggeun_q.append((nx, ny, time + 1))
        return "IMPOSSIBLE"

    # 메인 루프
    result = "IMPOSSIBLE"
    while sanggeun_q:
        fire()  # 불 확산
        result = move()  # 상근이 이동
        if result != "IMPOSSIBLE":
            break

    print(result)
