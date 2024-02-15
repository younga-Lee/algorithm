from collections import deque
def solution(board):
    answer = -1
    board = [list(board[_]) for _ in range(len(board))]
    # 첫 위치
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                sti, stj = i, j
            elif board[i][j] == 'G':
                xi, xj = i, j

    q = deque([(sti, stj, 0)])
    board[sti][stj] = 'V'
    while q:
        si, sj, cnt = q.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            k = 2
            ni, nj = si + di, sj + dj
            while 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != 'D':
                ni, nj = si + di * k, sj + dj * k
                k += 1

            if k != 2:
                if ni-di == xi and nj-dj == xj: #중지조건
                    return cnt + 1

                if board[ni-di][nj-dj] != 'V':
                    q.append((ni-di, nj-dj, cnt + 1))
                    board[ni-di][nj-dj] = 'V'

    return answer