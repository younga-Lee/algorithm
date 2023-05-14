n, game = input().split()
player = set()
dic = {'Y': 1, 'F': 2, 'O':3 }
for _ in range(int(n)):
    player.add(input())
print(len(player)//dic[game])