for _ in range(int(input())):
    phrase = input()
    if 'зайка' in phrase:
        print(phrase.find('зайка') + 1)
    else:
        print('Заек нет =(')