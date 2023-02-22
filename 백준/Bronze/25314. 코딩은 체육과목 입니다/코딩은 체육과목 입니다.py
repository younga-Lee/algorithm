n= int(input())
s = 0
if n%4 :
    s = n//4 + 1
else:
    s = n//4

print('long '*s + 'int')