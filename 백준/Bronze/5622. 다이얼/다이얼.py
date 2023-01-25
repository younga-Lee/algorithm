d = {2 : ['A','B','C'] , 3: ['D','E','F'] , 4: ['G','H','I'] ,5 : ['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'] ,8 : ['T','U','V'],9 : ['W','X' ,'Y','Z']}
word = input()
answer = 0
for i in range(2,10):
  for j in word:
    if j in d[i]:
      answer += i
print(answer + len(word))