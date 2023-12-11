def solution(bandage, health, attacks):
    current_time = 0 #현재시간
    attack_cnt = 0 #공격횟수
    h = health #현재체력
    cnt = 0 #연속 시전 횟수
    while attack_cnt < len(attacks):
        current_time += 1

        #공격당할 경우
        if current_time == attacks[attack_cnt][0]:
            h -= attacks[attack_cnt][1]
            cnt = 0
            #체력이 0면 끝
            if h <= 0 :
                return -1
            attack_cnt += 1
        #공격당하지 않을 경우 붕대감기
        else:
            h += bandage[1]
            cnt += 1
            if cnt == bandage[0]: #추가체력회복
                h += bandage[2]
                cnt = 0

            if h > health: #최대체력회복
                h = health
    return h