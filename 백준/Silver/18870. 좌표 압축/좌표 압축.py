n = int(input())
arr = list(map(int, input().split()))
s_arr = sorted(set(arr))

#시간 초과 -> 시간복잡도 O(n)
# for a in arr:
#     for i in range(len(s_arr)):
#         if a == s_arr[i]:
#             print(i, end = ' ')
#             break

#해싱 -> 시간복잡도 O(1)
dic = {s_arr[i]:i for i in range(len(s_arr))}
for a in arr:
    print(dic[a], end = ' ')