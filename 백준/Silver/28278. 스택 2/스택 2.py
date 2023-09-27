import sys
n = int(sys.stdin.readline())
stk = []
for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '1':
        stk.append(cmd[1])
    elif cmd[0] == '2':
        print(stk.pop() if len(stk) else -1)
    elif cmd[0] == '3':
        print(len(stk))
    elif cmd[0] == '4':
        print(0 if len(stk) else 1)
    elif cmd[0] == '5':
        print(stk[-1] if len(stk) else -1)