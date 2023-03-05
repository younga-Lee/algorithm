arr = [list(input().split()) for _ in range(5)]
say = []
for _ in range(5):
    num = list(input().split())
    for n in range(5):
        say.append(num[n])

#x로 대체하기
def check(s):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == say[s]:
                arr[i][j] = 'x'

#빙고 경우의 수
def bingo(arr):
    temp = 0
    arr2 = list(zip(*arr))
    for i in range(5):
        if ''.join(arr[i]) == 'xxxxx':
            temp += 1
        if ''.join(arr2[i]) == 'xxxxx':
            temp += 1
    if arr[0][0] == arr[1][1] == arr[2][2] == arr[3][3] == arr[4][4] == 'x':
        temp += 1
    if arr[0][4] == arr[1][3] == arr[2][2] == arr[3][1] == arr[4][0] == 'x':
        temp += 1
    if temp >= 3:
        return False

s = 0
while bingo(arr) is not False:
    check(s)
    bingo(arr)
    s += 1
print(s)