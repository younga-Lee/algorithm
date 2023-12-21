def solution(s, skip, index):
    answer = ''
    alpha = [chr(a) for a in range(97, 123)]*3
    for w in s:
        idx = alpha.index(w)
        cnt = 0
        while cnt != index:
            idx += 1
            if alpha[idx] not in list(skip):
                cnt += 1
        answer += alpha[idx]
    return answer