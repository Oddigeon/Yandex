n, m = int(input()), int(input())
names = set()

for _ in range(n + m):
    names.add(input())

result = 2 * len(names) - (n + m)

if result > 0:    
    print(result)
else:
    print('Таких нет')