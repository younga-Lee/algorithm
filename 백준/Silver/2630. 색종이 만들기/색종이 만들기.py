n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0

def check(x1, x2, y1, y2, size):
    global w,b
    flag = True
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[x1][y1] != arr[i][j]:
                flag = False
                break
        if flag is False:
            break

    if flag is True:
        if arr[x1][y1] == 0:
            w += 1
        else:
            b += 1
    else:
        size //= 2
        check(x1, x2-size, y1, y2-size, size)
        check(x1, x2-size, y1+size, y2, size)
        check(x1+size,x2, y1+size, y2, size)
        check(x1+size,x2, y1, y2-size, size)

check(0, n, 0, n, n)

print(w)
print(b)

