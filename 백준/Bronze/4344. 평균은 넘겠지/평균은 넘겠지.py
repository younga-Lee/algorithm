C = int(input())

for i in range(C):
  student = list(map(int, input().split()))
  n = student[0]
  score = student[1:]
  score_avg = sum(score)/n

  cnt = 0
  for i in score:
    if i > score_avg:
      cnt += 1
  print("{:.3f}%".format(round(cnt/n*100,4)))
