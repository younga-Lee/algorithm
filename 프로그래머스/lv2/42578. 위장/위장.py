def solution(clothes):
    ans = 1
    dic = {} #종류별 옷 딕셔너리 생성
    for v, k in clothes:
        if k in dic:
            dic[k] += [v]
        else:
            dic[k] = [v]
    
    for d in dic.keys():
        ans *= (len(dic[d])+1)
    return ans-1
    