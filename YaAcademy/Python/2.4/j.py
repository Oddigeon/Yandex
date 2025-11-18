# n = int(input())
# print('А Б В')
# for a in range(1, n):
#     if a > n:
#         break
#     for b in range(1, n):
#         if a + b > n:
#             break
#         for c in range(1, n):
#             if a + b + c == n:   
#                 print(a, b, c)


n = int(input())
print('А Б В')
for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if a + b + c == n:
                print(a, b, c)