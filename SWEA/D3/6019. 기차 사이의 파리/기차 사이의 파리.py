T = int(input())
for ts in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    time = D/(A+B) #A, B가 마주칠때까지 걸린 시간
    print(f'#{ts} {time*F}')