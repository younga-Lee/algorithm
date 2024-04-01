n, m = map(int, input().split())  # 사람의 수, 친구 관계의 수
arr = [[] for _ in range(n)]
ans = 0

# 그래프 구성
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

v = [0] * n


def dfs(idx, depth):
    if depth == 5:  # 최대 깊이가 5인지 확인
        return True

    for j in arr[idx]:
        if not v[j]:
            v[j] = 1
            if dfs(j, depth + 1):
                return True
            v[j] = 0
    return False


# 모든 노드에 대해서 DFS 수행
for i in range(n):
    v = [0] * n
    v[i] = 1
    if dfs(i, 1):
        ans = 1
        break

print(ans)
