for _ in range(10):
    ts = int(input())
    arr = [input() for _ in range(100)]
    mx = 0

    arr = [_ for _ in arr]
    arr2 = list(zip(*arr))

    for i in range(100): #한줄씩
        for k in range(100):
            for j in range(100-k+1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    if k > mx:
                        mx = k
                if arr2[i][j:j+k] == arr2[i][j:j+k][::-1]:
                    if k > mx:
                        mx = k

    print(f'#{ts}', mx)