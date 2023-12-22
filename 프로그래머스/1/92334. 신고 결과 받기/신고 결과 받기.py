'''
1. 유저, 신고 딕셔너리 id_list를 활용해 생성 
2. report기록
   user_do = 유저 ID : [유저가 신고한 ID ]
   user_get =  유저 ID : [유저가 신고받은 ID]
3. user_get 중 유저가 신고받은 ID가 k이상인 id (중복안됨) - target_id
4. user_do 중 target_id가 있으면 cnt +=1 ->result에 추가
'''

def solution(id_list, report, k):
    result = []
    user_do, user_get = dict(), dict()
    for i in id_list:
        user_do[i] = []
        user_get[i] = []
    for r in report:
        key, v = r.split(' ')
        user_do[key].append(v)
        user_get[v].append(key)
    target_id = []
    for i in id_list:
        if len(set(user_get[i])) >= k:
            target_id.append(i)
    for i in id_list:
        cnt = 0
        for j in target_id:
            if j in set(user_do[i]):
                cnt += 1
        result.append(cnt)
    return result