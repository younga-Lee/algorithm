def solution(n, words):
    num, rank = 0, 0
    lst = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in lst and lst[-1][-1] == words[i][0]:
            lst.append(words[i])
        else:
            num = i%n+1
            rank = i//n+1 
            break
    return [num, rank]