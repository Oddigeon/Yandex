# Найдётся всё

titles = []

for _ in range(int(input())):
    titles.append(input())

search = input().lower()

for title in titles:
    if search in title.lower():
        print(title)