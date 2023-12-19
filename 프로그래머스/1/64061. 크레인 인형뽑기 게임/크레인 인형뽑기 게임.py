def solution(board, moves):
    ans = 0
    stk = []
    for j in moves:
        for i in range(len(board)):
            b = board[i][j - 1]
            if b != 0:
                if stk:
                    a = stk.pop()
                    if a != b:
                        stk.append(a)
                        stk.append(b)
                    else:
                        ans += 2
                else:
                    stk.append(b)
                board[i][j - 1] = 0
                break
    return ans