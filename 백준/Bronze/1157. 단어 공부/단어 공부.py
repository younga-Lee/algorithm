word = input()
word = word.upper()

word_dict = dict()
for s in word:
  word_dict[s] = 0 #딕셔너리 만들기

for s in word:
  if s in word_dict:
    word_dict[s] += 1 #값 1씩 올리기

fre = [k for k,v in word_dict.items() if max(word_dict.values()) == v]
if len(fre) == 1:
  print(fre[0])
else:
  print('?')