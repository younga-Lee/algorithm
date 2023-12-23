'''
1. k일자까지는 모든 가수 점수 명예의전당
2. k일 이후에는 상위점수만 명예의 전당 (총k개만큼)
3. 명예의 전당 최하위점수 returun
'''
def solution(k, score):
    result = []
    reward = []
    for i in range(len(score)):
        if len(reward) < k:
            reward.append(score[i])
        else:
            reward = sorted(reward, reverse=True)
            if score[i] >= reward[-1]:
                reward.pop()
                reward.append(score[i])
        result.append(min(reward))
    return result