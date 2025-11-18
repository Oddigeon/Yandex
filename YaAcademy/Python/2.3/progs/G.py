a = int(input())
b = int(input())
x1, x2 = a, b

if a > b:
    while b:
        a, b = b, a % b
    nod = a
elif b > a:
    while a:
        b, a = a, b % a
    nod = b
else:
    nod = a
    
print((x1 * x2) // nod)