A = int(input())
B = int(input())
C = int(input())
n = str(A*B*C)
    
num_dict = dict()
for i in map(str,list(range(10))):
  num_dict[i] = 0
  for j in n:
    if j == i :
      num_dict[i] += 1
  print(num_dict[i]) #바로바로 출력하는 함수!!