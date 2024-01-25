import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    a = int(input())
    cnt_zero = [0]*(a+2)
    cnt_one = [0]*(a+2)

    cnt_zero[1] = 1
    cnt_one[0], cnt_one[0] = 1, 1
    for n in range(2, a+2):
        cnt_zero[n] = cnt_zero[n-1] + cnt_zero[n-2]
        cnt_one[n] = cnt_one[n - 1] + cnt_one[n - 2]

    print(cnt_one[a], cnt_zero[a])