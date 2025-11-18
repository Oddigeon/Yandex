n = int(input())
count = 1
num = 1

while num <= n:
    for i in range(count):
        if num > n:
            break
        print(num, end=' ')
        num += 1
    print()
    count += 1