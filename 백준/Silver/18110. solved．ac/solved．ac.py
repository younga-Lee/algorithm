#round는 오사오입이기 때문에 함수를 재정의해주어야 함

n = int(input())

def f_round(n):
    return int(n)+1 if n-int(n) >= 0.5 else int(n)

if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]

    arr.sort()
    ex = f_round(n*0.15) #제외되는 사람 수
    avg = sum(arr[ex:n-ex])/(n-2*ex) #절사평균
    print(f_round(avg))