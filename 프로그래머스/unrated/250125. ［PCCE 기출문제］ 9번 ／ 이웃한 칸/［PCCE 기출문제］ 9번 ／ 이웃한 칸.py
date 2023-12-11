def solution(board, h, w):
    answer = 0
    n = len(board)
    color = board[h][w]
    for dh, dw in [(0,1),(1,0),(0,-1),(-1,0)]:
        nh, nw = h + dh, w + dw
        if 0 <= nh < n and 0 <= nw < n:
            if color == board[nh][nw]:
                answer += 1
    return answer