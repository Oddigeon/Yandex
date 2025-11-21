# Очистка данных

while (title := input()):
    if not title.endswith('@@@'):
        if title.startswith('##'):
            title = title[2:]
        print(title)