import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'add':
        s.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        if s:
            s.remove(int(cmd[1]))
    elif cmd[0] == 'check':
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in s:
            s.remove(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    elif cmd[0] == 'all':
        s = {_ for _ in range(1, 21)}
    elif cmd[0] == 'empty':
        s = set()