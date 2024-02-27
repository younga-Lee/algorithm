n = int(input())
moves = []
def hanoi(n, start, target, mid, moves):
    if n == 1:
        moves.append((start, target))
        return

    #가장 큰 값 제외하고 나머지는 모두 보조 막대로 보내기, 보조 막대에 있는 건 모두 타겟으로
    hanoi(n-1, start, mid, target, moves) #디스크->보조막대
    moves.append((start, target)) #가장큰값 목적지
    hanoi(n-1, mid, target, start, moves) #보조막대 ->최종막대
hanoi(n, 1, 3, 2, moves)

print(len(moves))
for move in moves:
    print(move[0],move[1])