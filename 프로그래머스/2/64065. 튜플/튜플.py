def solution(s):
    num = sorted(s[2:len(s)-2].split('},{'), key = len)
    stk = []
    for i in range(len(num)):
        if stk:
            lst = num[i].split(',')
            for j in lst:
                if int(j) not in stk:
                    stk.append(int(j))
        else:
            stk.append(int(num[i]))

    return stk