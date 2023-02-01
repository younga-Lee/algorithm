import sys
input = sys.stdin.readline
n = int(input())

l = [tuple(map(int,input().split())) for _ in range(n)] # 좌표를 1차원 튜플로 만든 후, 리스트에 넣기
l_1 = sorted(l, key = lambda x: (x[0],x[1])) #x,y좌표 차례대로 정렬
 
for i in l_1:
    print(*i)