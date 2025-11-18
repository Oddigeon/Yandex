k = 0
while (word := input()) != 'Приехали!':
    if 'зайка' in word:
        k += 1
print(k)
