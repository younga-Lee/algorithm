n, m = map(int, input().split())
s = {input() for _ in range(n)}
person = []
for _ in range(m):
    p = input()
    if p in s:
        person.append(p)

print(len(person))
for ps in sorted(person):
    print(ps)