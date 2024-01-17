def solution(prices):
    ans = [0]*len(prices)
    stk = []
    for i in range(len(prices)):
        if not stk:
            stk.append(i)
        else:
            if prices[stk[-1]] <= prices[i]:
                stk.append(i)
            else:
                while stk and prices[stk[-1]] > prices[i]:
                    a = stk.pop()
                    ans[a] = i-a
                stk.append(i)
    while stk:
        a = stk.pop()
        ans[a] = len(prices)-1-a
    return ans