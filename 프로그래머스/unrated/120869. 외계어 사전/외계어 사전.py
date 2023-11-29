def solution(spell, dic):
    for d in dic:
        cnt = 0
        for s in spell:
            if d.count(s) == 1:
                d = d.replace(s,'1')
                cnt += 1
            else:
                break
        if cnt == len(spell) and d.isdigit() is True:
            return 1
    return 2