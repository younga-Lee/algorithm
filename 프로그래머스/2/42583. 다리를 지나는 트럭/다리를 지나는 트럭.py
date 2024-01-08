def solution(bridge_length, weight, truck_weights):
    tm = 1
    tw = truck_weights
    top = tw.pop(0)
    stk = [0]*(bridge_length-1) + [top]#다리에 있는 트럭
    cnt = top
    while stk != [0]*bridge_length or tw:
        if tw:
            top = tw[0]
        b = stk.pop(0)
        cnt -= b
        if len(stk)-stk.count(0) < bridge_length and cnt+top <= weight:
            if tw:
                a = tw.pop(0)
                stk.append(a)
                cnt += a
            else:
                stk.append(0)
        else:
            stk.append(0)
        tm += 1
    return tm