number = int(input())
max_total = 0
value = 0

for i in range(2, 11):
    x = number
    total = 0
    while x:
        total += x % i
        x //= i
    if total > max_total:
        max_total = total
        value = i

print(value)