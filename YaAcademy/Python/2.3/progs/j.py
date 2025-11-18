a = 0
b = 0

while (direction := input()) != 'СТОП':
    steps = int(input())
    match direction:
        case 'СЕВЕР':
            a += steps
        case 'ЮГ':
            a -= steps
        case 'ВОСТОК':
            b += steps
        case 'ЗАПАД':
            b -= steps
print(a, b, sep='\n')
