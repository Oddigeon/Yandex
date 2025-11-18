n = int(input())
count = 0

for i in range(n):
    num = int(input())
    k = num
    m = 0
    while num:
        m = m * 10 + num % 10
        num //= 10
    if k == m or k // 10 == 0:
        count += 1

print(count)