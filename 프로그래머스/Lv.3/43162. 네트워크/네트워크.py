def solution(n, computers):
    ans = 0
    stk = []
    while computers != [[0]*n]*n:
        #시작하는 위치
        for i in range(n):
            if computers[i] != [0]*n:
                stk.append(i)
                ans += 1
                break
        #노드 확인
        while stk:
            idx = stk[-1]
            computers[idx][stk[0]] = 0
            computers[idx][idx] = 0
            for j in range(n):
                if computers[idx][j] == 1:
                    computers[idx][j] = 0
                    stk.append(j)
                    break
            else:
                while stk:
                    top = stk.pop(0)
                    if computers[top] != [0] * n:
                        stk.append(top)
                        break

    return ans