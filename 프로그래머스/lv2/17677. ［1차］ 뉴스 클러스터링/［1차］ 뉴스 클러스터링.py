import math
def solution(str1, str2):
    answer = 0
    inter = 0
    str1 = str1.upper() #대소문자 구분안함
    str2 = str2.upper()
    
    #다중집합
    s1 = [str1[i1:i1+2] for i1 in range(len(str1)-1) if str1[i1:i1+2].isalpha()]
    s2 = [str2[i2:i2+2] for i2 in range(len(str2)-1) if str2[i2:i2+2].isalpha()]
    
    #공집합이면 1
    if s1 == [] and s2 == []:
        return 65536
    
    N1, N2 = len(s1), len(s2)
    for one in range(N1):
        for two in range(len(s2)):
            if s1[one] == s2[two]:
                inter += 1
                s2.remove(s2[two])
                break
            
    #자카드 유사도
    uni = N1 + N2 - inter
    if inter == uni:
        return 65536
    
    answer = inter/uni
    return math.trunc(answer*65536)