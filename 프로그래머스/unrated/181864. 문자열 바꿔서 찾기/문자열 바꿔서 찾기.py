def solution(myString, pat):
    newString = ''
    for _ in myString:
        if _ == 'A':
            newString += 'B'
        else:
            newString += 'A'
    if pat in newString:
        return 1
    else:
        return 0
    