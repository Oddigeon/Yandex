n = int(input())
fin_nod = 1

for i in range(1):
    a = int(input())
    b = int(input())
    if a > b:
        while b:
            a, b = b, a % b
        nod = a
    elif a < b:
        while a:
            b, a = a, b % a
        nod = b
    else:
        nod = a
if n == 2:
    print(nod)
else:
    for i in range(n - 2):
        x = int(input())
        if nod > x:
            while x:
                nod, x = x, nod % x
            fin_nod = nod
        elif nod < x:
            while nod:
                x, nod = nod, x % nod
            fin_nod = x
        else:
            fin_nod = nod

    print(fin_nod)
