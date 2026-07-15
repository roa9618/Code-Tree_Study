n = input()

words = ["apple", "banana", "grape", "blueberry", "orange"]
count = 0

for word in words :
    if word[2] == n or word[3] == n :
        count += 1
        print(word)

print(count)