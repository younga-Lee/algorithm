cro_alpha = input() #문자열로 가져옴

change = ['c=' ,'c-','dz=','d-','lj','nj','s=','z=']

for s in change:
  cro_alpha = cro_alpha.replace(s,'!')
print(len(cro_alpha))