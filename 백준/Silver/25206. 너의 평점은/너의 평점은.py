score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
sum, cnt = 0, 0
for _ in range(20):
    subject, school, grade = input().split()
    school = float(school)
    if grade in score.keys():
        sum += school*score[grade]
        cnt += school
print('%8.6f'%(sum/cnt))