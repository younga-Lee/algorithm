n = int(input())
for _ in range(n):
    word = input()
    ans, top = 'YES', -1
    stack = []

    for s in word:
        if s == '(' :
            stack.append(s)
            top += 1
        elif s == ')' and top > -1:
            stack.pop()
            top -= 1
        else:
            ans = 'NO'

    if stack != []: ans = 'NO'
    print(ans)
