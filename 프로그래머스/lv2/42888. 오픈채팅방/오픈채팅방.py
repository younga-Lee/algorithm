def solution(record):
    answer = []
    name = {}
    come = []
    for i in range(len(record)):
        r = record[i].split()
        if r[0] != 'Change':
            come.append([r[0], r[1]])
        if r[0] != 'Leave':
            name[r[1]] = r[2]
    
    for j in range(len(come)):
        if come[j][0] == 'Enter':
            answer.append(str(name[come[j][1]]) + "님이 들어왔습니다.")
        else:
            answer.append(str(name[come[j][1]]) + "님이 나갔습니다.")
            
    return answer