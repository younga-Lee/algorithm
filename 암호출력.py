def bit(t):
    output = ''
    for i in range(3, -1, -1):
        output += '1' if t & (1 << i) else '0' #t의 i번째 비트가 1인지 아닌지
    return output

T = int(input())

for tc in range(1, T+1):
    num = input()

    #16진수 -> 2진수
    arr = ''
    for n in num:
        if n.isdigit():
            t = ord(n) - ord('0')
            arr += bit(t)
        else:
            t = ord(n) - ord('A') + 10
            arr += bit(t)

    #암호 범위를 찾아보자
    idx = 0
    for j in range(len(arr)-1, -1, -1):
        if '1' == arr[j]:
            idx = j
            break
    arr = arr[idx%6 + 1:idx+1]

    #암호비트 패턴찾기
    secret_dct = {'001101': 0, '010011': 1, '111011': 2, '110001': 3, '100011':4, '110111':5, '001011':6, '111101':7, '011001':8, '101111':9}
    ans = []
    for p in range(0, len(arr), 6):
        code = arr[p: p+6]
        if code in secret_dct:
            ans.append(secret_dct[code])

    print(f'#{tc}', *ans)