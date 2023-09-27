import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

#문자열 P
P = ''
for i in range(2*n+1):
    if i%2:
        P += 'O'
    else:
        P += 'I'

cnt = 0
#어딨니~
for i in range(m-len(P)+1):
    if s[i] == 'I':
        if s[i:i+len(P)] == P:
            cnt += 1
print(cnt)