def solution(citations):
    lst = sorted(citations, reverse = True)
    ans = 0
    i = 0
    while i != len(lst):
        if lst[i] <= ans:
            return ans
        ans += 1
        i += 1
    return ans