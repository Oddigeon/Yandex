# Кашееды

n, m = int(input()), int(input())
ms, os = set(), set()

for _ in range(n):
    ms.add(input())

for _ in range(m):
    os.add(input())

counter = len(ms & os)

if counter > 0:
    print(counter)
else:
    print('Таких нет')