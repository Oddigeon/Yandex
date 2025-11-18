# Числовая змейка 2.0

n = int(input())
m = int(input())
max_num = n * m
width = 0

while max_num:
    width += 1
    max_num //= 10

for row in range(n):
    for col in range(m):
        num = (col * n + row + 1) if col % 2 == 0 else (col * n + n - row)
        print(f'{num:>{width}}', end=' ')
    print() 