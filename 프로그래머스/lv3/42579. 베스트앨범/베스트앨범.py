def solution(genres, plays): 
    ans = []
    dic1 = dict() 
    dic2 = dict() 
    for i in range(len(genres)):
        if genres[i] not in dic1:
            dic1[genres[i]] = plays[i]
        else:
            dic1[genres[i]] += plays[i]
    
        if genres[i] not in dic2:
            dic2[genres[i]] = [(i, plays[i])]
        else:
            dic2[genres[i]] += [(i, plays[i])]
    genre = sorted(dic1.items(), key=lambda x : x[1], reverse= True)
    
    gr = []
    for a in range(len(genre)):
        gr.append(genre[a][0])
    
    for g in gr:
        for num in dic2[g]:
            tmp = sorted(dic2[g], key= lambda x: (x[1], -x[0]))
        if len(tmp) >= 2:
            ans.append(tmp.pop()[0])
            ans.append(tmp.pop()[0])
        elif len(tmp) == 1:
            ans.append(tmp.pop()[0])
    return ans