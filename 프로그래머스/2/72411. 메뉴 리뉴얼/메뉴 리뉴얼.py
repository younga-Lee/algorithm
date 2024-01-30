from itertools import combinations
def solution(orders, course):
    answer = []
    dic = dict()

    #모든 주문에 가능한 조합
    for order in orders:
        for c in course:
            for comb in combinations(sorted(order), c):
                comb_str = ''.join(comb)
                if comb_str in dic:
                    dic[comb_str] += 1
                else:
                    dic[comb_str] = 1

    #가장 높은 빈도수
    for c in course:
        tmp = []
        for k, v in dic.items():
            if len(k) == c and v >= 2:
                tmp.append((k,v))
        tmp = sorted(tmp, key=lambda x:-x[1])
        if tmp:
            top = tmp[0][1]
            while tmp:
                a = tmp.pop(0)
                if top == a[1]:
                    answer.append(a[0])

    return sorted(answer)