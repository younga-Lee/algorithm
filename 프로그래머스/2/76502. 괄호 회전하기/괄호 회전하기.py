def check(lst):
    dic = {')': '(', '}': '{', ']': '['}
    stk = []
    flag = 0
    while lst:
        a = lst.pop(0)
        if a in ['[', '(', '{']:
            stk.append(a)
        else:
            if stk and dic[a] == stk.pop():
                pass
            else:
                flag = 1
                break
    if stk == [] and flag == 0:
        return 1
    return 0

def solution(s):
    ans = 0
    s = list(s)
    for _ in range(len(s)):
        lst = s.copy()
        if check(lst) == 1:
            ans += 1
        s.append(s.pop(0))
    return ans