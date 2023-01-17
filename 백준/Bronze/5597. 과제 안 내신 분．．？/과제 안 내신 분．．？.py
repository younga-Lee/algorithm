student = list(range(1,31))

for i in range(28):
    a = int(input())
    student.remove(a)
print(min(student), max(student))