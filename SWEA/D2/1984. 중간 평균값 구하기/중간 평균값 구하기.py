T = int(input()) #테스트 케이스

for tc in range(1,T+1):
    l = list(map(int,input().split()))
    avg = round(sum(sorted(l)[1:9])/8)
    print(f'#{tc} {avg}')