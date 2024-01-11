def solution(begin, target, words):
    N = len(target)
    ans = 10 ** 10
    visited = [1] * len(words)

    def dfs(cnt, begin):
        nonlocal ans
        if begin == target:
            ans = min(ans, cnt)
            return ans
        for i in range(len(words)):
            if visited[i] == 1:
                diff = 0
                for j in range(len(target)):
                    if begin[j] != words[i][j]:
                        diff += 1
                if diff == 1:                
                    visited[i] = 0
                    dfs(cnt + 1, words[i])
                    visited[i] = 1

    dfs(0, begin)

    if ans == 10 ** 10:
        return 0
    else:
        return ans