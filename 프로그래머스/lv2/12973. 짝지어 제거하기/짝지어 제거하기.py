def solution(s):
    stk = []
    
    for i in s:
        if stk != [] and stk[-1] == i:
            stk.pop()
        else:
            stk.append(i)
    return 1 if stk == [] else 0