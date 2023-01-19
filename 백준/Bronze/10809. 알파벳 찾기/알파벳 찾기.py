word = input()
init = {i:-1 for i in list(range(97,123))}

for s in range(len(word)):
  if (ord(word[s]) in init) and (init[ord(word[s])] == -1) : 
    init[ord(word[s])] = s
print(' '.join(list(map(str, init.values()))))