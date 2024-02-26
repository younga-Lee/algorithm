
def solution(files):
    answer = []
    for file in files:
        header = ''
        i = 0
        while True:
            if file[i].isdigit() is False:
                header += file[i]
                i += 1
            else:
                break

        num = ''
        while i != len(file):
            if file[i].isdigit() is True:
                num += file[i]
                i += 1
            else:
                break

        tail = file[i:]
        answer.append((header, num, tail))

        answer = sorted(answer, key=lambda x:[str.lower, int(x[1])])
    ans = []
    for a, b, c in answer:
        ans.append(a+b+c)
    return ans
