n = int(input())
dic = dict()
for _ in range(n):
    title = input()
    if title in dic:
        dic[title] += 1
    else:
        dic[title] = 0
print(sorted(dic.items(), key=lambda x:[-x[1], x[0]])[0][0])