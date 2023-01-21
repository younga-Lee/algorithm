T = int(input())
for t in range(T):
  n , string = input().split()
  for s in string:
    p = int(n)*s
    print(p, end = '')
  print()