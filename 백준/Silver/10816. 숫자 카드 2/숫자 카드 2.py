import sys

input = sys.stdin.readline

n = int(input())
lst1 = list(map(int, input().split()))

m = int(input())
lst2 = list(map(int, input().split()))

count_dict = {}
for num in lst1:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = []
for num in lst2:
    result.append(count_dict.get(num, 0)) #없으면 0

print(*result)
