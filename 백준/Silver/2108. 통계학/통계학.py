import statistics as sts
import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
print(int(round(sts.mean(lst), 0)))
print(sts.median(lst))

l = sorted(sts.multimode(lst))
if len(l) != 1:
    print(l[1])
else:
    print(l[0])
print(max(lst)-min(lst))