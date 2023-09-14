n, m = map(int, input().split())
pwds = dict()
for _ in range(n):
    site, pwd = input().split()
    pwds[site] = pwd
for i in range(m):
    s = input()
    print(pwds[s])