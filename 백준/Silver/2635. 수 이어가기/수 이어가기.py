n = int(input())

def check(lst):
  j, new = 1,0
  while new >= 0:
    new = lst[j-1]-lst[j]
    lst.append(new)
    j += 1
    
    
new = 0
ans = []
for i in range(1,n+1):
  lst = [n] #첫번째수
  lst.append(i) #두번째 수 
  check(lst)
  ans.append(lst)
    
mx = max(ans, key = len)
print(len(mx)-1)
print(*mx[:-1])