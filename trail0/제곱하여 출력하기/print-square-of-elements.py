N = int(input())
num = list(map(int, input().split()))

print(*[i ** 2 for i in num])