def solution(friends, gifts):
    give = dict()
    take = dict()
    ans = dict()
    n = len(friends)
    for f in friends:
        give[f] = []
        take[f] = []
        ans[f] = 0

    for gift in gifts:
        g, t = gift.split()
        give[g].append(t)
        take[t].append(g)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if give[friends[i]].count(friends[j]) != give[friends[j]].count(friends[i]):
                if give[friends[i]].count(friends[j]) > give[friends[j]].count(friends[i]):
                    ans[friends[i]] += 1
                else:
                    ans[friends[j]] += 1

            else:
                if len(give[friends[i]])-len(take[friends[i]]) != len(give[friends[j]])-len(take[friends[j]]):
                    if len(give[friends[i]])-len(take[friends[i]]) > len(give[friends[j]])-len(take[friends[j]]):
                        ans[friends[i]] += 1
                    else:
                        ans[friends[j]] += 1
    
    return max(ans.values())