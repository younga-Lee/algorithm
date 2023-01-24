x = int(input())

if 1 <= x < 100:
  print(x)
else:
  total = 99
  for i in range(100,x+1):
    i = str(i)
    if int(i[0]) + int(i[2]) == int(i[1])*2:
      total += 1
  print(total)