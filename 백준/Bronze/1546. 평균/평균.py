N = int(input())
score = list(map(int, input().split()))

M = max(score)
print(sum([i/M*100 for i in score])/N)

