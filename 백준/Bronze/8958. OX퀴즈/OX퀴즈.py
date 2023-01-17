T = int(input())

for i in range(T):
    q = input()
    history = []
    score = []
    
    if q[0] == 'O':
        score.append(1)
        history.append('O')
    else:
        score.append(0)
        history.append('X')
    for s in range(1, len(q)):
        if q[s] == 'O':
            history.append(q[s])
            if history[s-1] == q[s]:
                score.append(score[s-1]+1)
            else:
                score.append(1)
        else:
            score.append(0)
            history.append(q[s])
    print(sum(score))
