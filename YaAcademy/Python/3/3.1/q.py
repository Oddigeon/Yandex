# А роза упала на лапу Азора 5.0

text = input()
replace_word = text.lower().replace(' ', '')

if replace_word[::-1] == replace_word:
    print('YES')
else:
    print('NO')