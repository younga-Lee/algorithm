N = input()
total = 0
new = N

while True:

    if int(new) < 10:
        new = '0'+new   
    new = new[-1] + str(int(new[0]) + int(new[-1]))[-1]
    total += 1
    
    if int(new) == int(N):
        print(total)
        break