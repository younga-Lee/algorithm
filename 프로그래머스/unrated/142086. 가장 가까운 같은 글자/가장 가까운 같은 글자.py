def solution(s):
    answer = []
    stk = {} #사용한 문자열
    for i in range(len(s)):
        if s[i] not in stk: #사용하지 않았다면
            stk[s[i]] = i
            answer.append(-1)
        else: #사용했다면
            answer.append(i - stk[s[i]])
            stk[s[i]] = i #갱신
    return answer