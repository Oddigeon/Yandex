a = int(input())
b = int(input())
step = 1
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    step = -1 
    for i in range(a, b - 1, step):
        print(i, end=' ')