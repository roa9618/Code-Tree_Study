nums = list(map(int, input().split()))

for i in range(2, 10) :
    ex = nums[i - 2] + nums[i - 1]

    if ex >= 10 :
        nums.append(ex % 10)
    else :
        nums.append(ex)

print(*[i for i in nums])