N = int(input())
num = list(map(int, input().split()))

num.reverse()

print(*[i for i in num if i % 2 == 0], sep = ' ')