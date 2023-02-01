n = int(input())

l = [input() for i in range(n)]
l_0 = list(set(l))
l_1 = sorted(l_0)
l_2 = sorted(l_1, key = len)

print(*l_2, sep='\n')