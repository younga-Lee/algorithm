str = input()
ans = ''
for s in str:
    if s.islower():
        ans += s.upper()
    else:
        ans += s.lower()
print(ans)