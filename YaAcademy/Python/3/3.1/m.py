# Массовое возведение в степень

numbers = []

for _ in range(int(input())):
    numbers.append(input())

degree = int(input())

for number in numbers:
    print(int(number) ** degree)