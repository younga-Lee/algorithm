import math
def solution(progresses, speeds):
    st = 0
    ans = []
    cnt = 0
    while st != len(progresses):
        tm = math.ceil((100-progresses[st])/speeds[st])
        for i in range(st, len(progresses)):
            progresses[i] += speeds[i]*tm
        for j in range(st, len(progresses)):
            if progresses[j] < 100:
                ans.append(cnt)
                cnt = 0
                break
            else:
                st += 1
                cnt += 1
        if cnt != 0:
            ans.append(cnt)
    return ans