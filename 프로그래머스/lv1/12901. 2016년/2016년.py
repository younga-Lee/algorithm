def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    num = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    t = 0
    
    for i in range(0,a):
        t += num[i]
    t += b
        
    return day[t%7-1]