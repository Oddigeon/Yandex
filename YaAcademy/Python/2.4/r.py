# Новогоднее настроение 2.0

limit = int(input())

counter = 0
width = 1
max_length = 0

while counter <= limit:
    string_length = 0
    for position in range(width):
        counter += 1
        if counter <= limit:
            string_length += len(str(counter))
        if position < width - 1 and counter < limit:
            string_length += 1

    if max_length < string_length:
        max_length = string_length

    width += 1

counter = 0
width = 1

while counter <= limit:
    string = ''
    for position in range(width):
        counter += 1
        if counter <= limit:
            string += str(counter)
        if position < width - 1 and counter < limit:
            string += ' '
    width += 1
    print(f'{string:^{max_length}}')

# не зачли

# max_number =  int(input())
# row = 1
# col = 1
# number = 1
# row_value = ''

# while number <= max_number:
#     row_value = ''
#     while col <= row and number <= max_number:
#         row_value += str(number) + (' ' if col < row and number < max_number else '')
#         col += 1
#         number += 1
#     row += 1
#     col = 1
# width = len(row_value)

# number = 1
# while number <= max_number:
#     numbers = ''
#     for i in range(col):
#         if number > max_number:
#             break
#         numbers = numbers + str(number) + (' ' if col < row and number < max_number else '')
#         number += 1
#     print(f'{numbers:^{width}}', end='')
#     print()
#     col += 1