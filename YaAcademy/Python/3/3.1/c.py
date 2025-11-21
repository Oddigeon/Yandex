# Анонс новости

length = int(input())
n = int(input())

for i in range(n):
    phrase = input()
    if len(phrase) <= length:
        print(phrase)
    else:
        print(f'{phrase[:length - 3]}...', end='\n')