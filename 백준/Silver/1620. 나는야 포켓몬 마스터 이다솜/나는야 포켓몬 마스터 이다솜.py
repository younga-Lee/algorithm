import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dic_num = dict()
dic_word = dict()
for i in range(n):
    poketmon = input().strip()
    dic_word[poketmon] = i+1
    dic_num[i+1] = poketmon

for _ in range(m):
    a = input().strip()
    if a.isdigit():
        print(dic_num[int(a)])
    else:
        print(dic_word[a])