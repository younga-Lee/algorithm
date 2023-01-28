T = int(input())

answer = []
for t in range(T):
    n = int(input())
    if n == 0:
        answer.pop()
    else:
        answer.append(n)
print(sum(answer))