n = int(input())
count = 0

for i in range(n):
    x = int(input())
    if x == 1:
        count += 1
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            count += 1
            break
print(n - count)