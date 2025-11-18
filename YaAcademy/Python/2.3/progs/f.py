a = int(input())
b = int(input())
if a > b:
    while b:
        a, b = b, a % b
    print(a)
elif a < b:
    while a:
        b, a = a, b % a
    print(b)
else:
    print(a)