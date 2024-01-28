dic = {')':'(', ']': '['}
while True:
    word = input()
    if word == '.':
        break
    ans = 'yes'
    stk = []
    for i in range(len(word)):
        if word[i] in ['(',')','[',']']:
            if word[i] in ['(','[']:
                stk.append(word[i])
            else:
                if stk and stk.pop() == dic[word[i]]:
                    pass
                else:
                    ans = 'no'
                    break
    if stk:
        ans = 'no'
    print(ans)