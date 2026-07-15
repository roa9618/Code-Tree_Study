N = 0

while N != 25 :
    N = int(input())

    if N > 25 :
        print("Lower")
    elif N < 25 :
        print("Higher")
    else :
        print("Good")
        break