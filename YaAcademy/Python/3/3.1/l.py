# Меню питания

dishes = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']

for day in range(days := int(input())):
    today = dishes[day % len(dishes)]
    print(today)

    