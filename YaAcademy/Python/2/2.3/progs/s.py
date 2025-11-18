num = 500
delta = num // 2
print(num)

while (answer := input()) != 'Угадал!':
    if answer == 'Больше':
        num += delta
    if answer == 'Меньше':
        num -= delta
    if delta >= 2:
        delta = (delta + 1) // 2
    print(num)