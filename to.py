T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count = [0]*1001

    for _ in range(N):
        num, a, b = map(int, input().split())
        if num == 1:
            for i in range(a, b+1):
                count[i] += 1
        elif num == 2:
            for j in range(a, b+1, 2):
                count[j] += 1
        elif num == 3:
            if a%2:
                for k in range(a, b+1):
                    if k%3 == 0 and k%10 !=0:
                        count[k] += 1
            else:
                for k in range(a, b + 1):
                    if k%4 == 0:
                        count[k] += 1
    print(f'#{tc} {max(count)}')
