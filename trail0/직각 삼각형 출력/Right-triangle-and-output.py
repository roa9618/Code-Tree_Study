N = int(input())
num = 0

for i in range(N) :
    for j in range(i + i + 1) :
        print('*', end = '')
    print()

    num += i