# Редизайн таблицы умножения

size = int(input())
ceil_width = int(input())

string_length = size * ceil_width + (size - 1)

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f'{(row * column):^{ceil_width}}', end='')
        if column == size:
            print()
        else:
            print('|', end='')
    if row != size:
        print('-' * string_length)