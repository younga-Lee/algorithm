t = int(input())
for tc in range(t):
    n = int(input())

    #의상 해싱
    clothes = dict()
    for _ in range(n):
        cloth, tp = input().split()
        if tp not in clothes.keys():
            clothes[tp] = {cloth}
        else:
            clothes[tp].add(cloth)

    #의상 개수
    cnt = 1
    for k, v in clothes.items():
        cnt *= len(clothes[k])+1
    print(cnt-1)