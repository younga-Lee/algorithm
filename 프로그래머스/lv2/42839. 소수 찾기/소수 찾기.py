from itertools import combinations, permutations
def solution(numbers):
    ans = []
    res = []
    for i in range(1, len(numbers)+1):
        ans += list(combinations(numbers, i))
    for a in range(len(ans)):
        res += list(permutations(ans[a]))
    #고유의 숫자로 변환
    cnt = set()
    for j in range(len(res)):
        n = int(''.join(res[j]))
        cnt.add(n)
    #소수를 구해보자
    cnt = list(cnt)
    final = 0
    f = []
    for k in range(len(cnt)):
        if cnt[k] != 0 and cnt[k] != 1:
            for m in range(2, cnt[k]):
                if cnt[k]%m == 0:
                    break
            else:
                final += 1
                f.append(cnt[k])
    return final