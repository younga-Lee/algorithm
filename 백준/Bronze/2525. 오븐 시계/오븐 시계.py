h,m = map(int, input().split())
a = int(input())

h = h + (m+a)//60
m = (m+a)%60

if h >= 24:
    h = h - 24

print(h, m)