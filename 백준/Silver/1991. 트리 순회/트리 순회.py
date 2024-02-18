'''
전위 순회 : 부모 - 왼 - 오
중위 순회 : 왼 - 부모 - 오
후위 순회 : 왼 - 오 - 부모
'''

'''
왼쪽이 없을 때까지 파고들고, 왼쪽 없다면 그 전 부모노드의 오른쪽 노드
A에서 왼쪽 -> B
B에서 왼쪽 -> D
D에서 왼쪽 x, 오른쪽 x
B에서 오른쪽 x
A에서 오른쪽 -> C
C에서 왼쪽 -> E
E에서 왼쪽 x, 오른쪽 x

A를 q에 넣기

A왼쪽 : B
 오른쪽 : C

만약 왼쪽이 있다면 -> 

'''
n = int(input())
dic = {}
for _ in range(n):
    node, l, r = input().split()
    dic[node] = (l, r)
ans1, ans2, ans3 = '', '',''

def pre(start_node):
    global ans1
    ans1 += start_node
    if dic[start_node][0] != '.':
        pre(dic[start_node][0])
    if dic[start_node][1] != '.':
        pre(dic[start_node][1])

def mid(start_node):
    global ans2
    if dic[start_node][0] != '.':
        mid(dic[start_node][0])
    ans2 += start_node
    if dic[start_node][1] != '.':
        mid(dic[start_node][1])

def last(start_node):
    global ans3
    if dic[start_node][0] != '.':
        last(dic[start_node][0])
    if dic[start_node][1] != '.':
        last(dic[start_node][1])
    ans3 += start_node

pre('A')
mid('A')
last('A')
print(ans1)
print(ans2)
print(ans3)