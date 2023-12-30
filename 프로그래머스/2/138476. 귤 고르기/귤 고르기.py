from collections import Counter
def solution(k, tangerine):
    ans = 1
    lst = sorted(Counter(tangerine).items(), key = lambda x:-x[1])
    for key, value in lst:
        if k-value > 0:
            ans += 1
            k -= value
        else:
            return ans

