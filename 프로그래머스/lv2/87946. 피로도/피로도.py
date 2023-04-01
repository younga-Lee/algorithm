from itertools import permutations as perm

def solution(k, dungeons):
    answer = -1
    path = perm(dungeons)
    for p in path:
        a = k #피로도, cnt 초기화
        cnt = 0
        for i in range(len(dungeons)):
            if a >= p[i][0]:
                a -= p[i][1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
    return answer