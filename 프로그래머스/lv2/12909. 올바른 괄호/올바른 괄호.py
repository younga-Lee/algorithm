def solution(s):
    answer = True
    stk = []
    for i in s:
        if i == '(':
            stk.append('(')
        if i == ')':
            if stk and stk.pop() == '(':
                pass
            else:
                return False
    if stk == []:
        return True
    else:
        return False