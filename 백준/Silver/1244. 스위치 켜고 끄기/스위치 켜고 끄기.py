switch_cnt = int(input())
switch_list = list(map(int, input().split()))
student_cnt = int(input())

def change_switch(n): #스위치상태 바꾸는 함수
  if switch_list[n] == 1: 
    switch_list[n] = 0
  else:
    switch_list[n] = 1
  return switch_list

for ts in range(student_cnt):
  gender, num = map(int, input().split())
  #남학생
  if gender == 1: 
    for i in range(1, (switch_cnt//num)+1): #배수의 개수
      n= i*num -1
      change_switch(n)
  #여학생
  elif gender == 2:
    n = num-1 #리스트 인덱스
    change_switch(n) #부여받은 번호의 스위치 변경

    if num > len(switch_list)/2 :
      num = len(switch_list)-num+1

    for j in range(1,num):
      if switch_list[n-j] == switch_list[n+j]: #대칭이라면 스위치 상태 변경
        change_switch(n-j)
        change_switch(n+j)
      else:
        break
      
for i in range(1, switch_cnt+1):
    print(switch_list[i-1], end = " ")
    if i % 20 == 0 :
        print()