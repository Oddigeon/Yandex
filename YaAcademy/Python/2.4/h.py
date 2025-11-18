count = int(input())

best_name = ''
best_sum = 0
for i in range(count):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if summa >= best_sum:
        best_sum = summa
        best_name = name

print(best_name)

# n = int(input())
# name = None
# max_sum = 0
# num_sum = 0

# for i in range(n):
#     name1 = input()
#     num = int(input())
#     while num > 0:
#         num_sum += num % 10
#         num //= 10
#     if num_sum >= max_sum:
#         max_sum = num_sum
#         name = name1
# print(name)
