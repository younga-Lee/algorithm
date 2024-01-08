def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:
        stk = list(skill).copy()
        flag = 1
        for i in range(len(tree)):
            if stk:
                if tree[i] in stk:
                    if tree[i] == stk[0]:
                        stk.pop(0)
                    else:
                        flag = 0
                        break
            else:
                break
        if flag == 1:
            ans += 1
    return ans