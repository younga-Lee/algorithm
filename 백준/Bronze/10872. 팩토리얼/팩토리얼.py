n = int(input())

def fac(n):
    answer = 1
    if n != 0:
        answer = n * fac(n-1)
        n -=1 
    return answer

print(fac(n))