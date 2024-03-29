from collections import deque
n = int(input()) #전체사람의 수
tx, ty = map(int, input().split()) #타겟
m = int(input()) #관계 수

#그래프로 만들기
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

#촌수 계산하기
count= [0]*(n+1)
count[tx] = 1
q = deque([(tx, 0)])

def dfs():
    while q:
        tx, ans = q.popleft()
        if ty == tx:
            return ans
        for node in arr[tx]:
            if count[node] == 0:
                count[node] = 1
                q.append((node, ans+1))
    return -1
print(dfs())
