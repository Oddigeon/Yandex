# RLE

text = input()
reference = text[0]
count = 1
text = text[1:] + '_'

for digit in text:
    if digit == reference:
        count += 1
    else:
        print(f'{reference} {count}')
        reference = digit
        count = 1
        