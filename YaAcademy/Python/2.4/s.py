n = int(input())

width = len(str((n + 1) // 2))

for row in range(n):
    for col in range(n):
        print(f'{(min(row + 1, col + 1, n - row, n - col)):>{width}}', end=' ')
    print()