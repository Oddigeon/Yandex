# Числовая змейка

n = int(input())
m = int(input())
max_num = n * m
width = 0

while max_num:
    width += 1
    max_num //= 10

for row in range(n):
    for col in range(m):
        num = (row * m + col + 1) if row % 2 == 0 else (row * m + m - col)
        print(f'{num:>{width}}', end=' ')
    print()