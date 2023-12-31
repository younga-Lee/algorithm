def solution(numbers):
    ans = []
    for i in range(len(numbers)-1, -1, -1):
        stk = []
        for j in range(i, len(numbers)):
            if numbers[j] > numbers[i]:
                stk.append(numbers[j])
                break
        if stk:
            ans.append(stk[0])
        else:
            ans.append(-1)
    return ans[::-1]