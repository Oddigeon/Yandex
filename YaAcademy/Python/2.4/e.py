n = int(input())
count = 0

for _ in range(n):
    counted = False
    while (place := input()) != 'ВСЁ':
        if place == 'зайка' and counted is False:
            count += 1
            counted = True
print(count)