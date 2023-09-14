A, B, V = map(int, input().split())
if (V-A)%(A-B) == 0:
    ans = (V-A)//(A-B) + 1
else:
    ans = (V-A)//(A-B) + 2
print(ans)

#시간 초과
# day = 0
# ps = 0
# while ps < V:
#     ps += A
#     if ps - B > 0 :
#         ps -= B
#     else:
#         ps = 0
#     day += 1
# print(day-1)
