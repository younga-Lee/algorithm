def solution(N, stages):
    stages = [0]+stages #번호 맞추기 위함
    result = {}
    total = len(stages)-1
    for i in range(1, N+1): #i번 스테이지
        fail = 0
        if total != 0:
            for j in range(len(stages)):
                if stages[j] == i:
                    fail += 1
            fail_rate = fail/total #실패율
            result[i] = fail_rate
            total -= fail
        else:
            result[i] = 0

    result = sorted(result.items(), key=lambda x:(-x[1], x[0]))
    ans = []
    for a in range(N):
        ans.append(result[a][0])
    return ans