n, r, c = map(int, input().split())

def check(size, i, j):
    if size == 1: #종료 조건 : 탐색영역 크기가 가장 작을 경우
        return 0
    size //= 2

    #각 사분면에 해당하는지 탐색
    if r < i+size and c < j+size:
        return check(size, i, j)
    elif r < i+size and c >= j+size:
        return size*size + check(size, i, j+size)
    elif r >= i+size and c<j+size:
        return 2*size*size + check(size, i+size, j)
    else:
        return 3*size*size + check(size, i+size, j+size)
print(check(2**n,0, 0))
