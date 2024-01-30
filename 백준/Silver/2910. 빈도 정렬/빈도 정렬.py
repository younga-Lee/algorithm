from collections import Counter
import sys
input = sys.stdin.readline

n, c = map(int, input().split()) #숫자개수, 최대값 숫자
lst = list(map(int, input().split()))

for k, v in Counter(lst).most_common():
    for _ in range(v):
        print(k, end = ' ')