n = int(input())
lst1 = sorted(list(map(int, input().split())))
m = int(input())
lst2 = list(map(int, input().split()))

def search(l, r, target):
    while l <= r:
        mid = (r+l)//2
        if lst1[mid] < target:
            l= mid+1
        elif lst1[mid] > target:
            r = mid-1
        else:
            return True
    return False

for num in lst2:
    ans = 0 #존재하지 않음
    if search(0, n-1, num) is True:
        ans = 1
    print(ans)