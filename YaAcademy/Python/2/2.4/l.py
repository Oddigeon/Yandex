n = int(input())
m = int(input())
max_number = n * m
width = 0

while max_number:
    width += 1
    max_number //= 10

for row in range(n):
    for col in range(m):
        num = row * m + col + 1
        print(f'{num:>{width}}', end=' ')
    print()