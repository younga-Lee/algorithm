n = int(input()) # 색종이의 수
b = 0
arr = []
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            if (i, j) in arr:
                b += 1
            else:
                arr.append((i, j))
print(n*100 - b)