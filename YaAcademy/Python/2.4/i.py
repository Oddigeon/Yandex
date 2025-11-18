n = int(input())
num = ''

for i in range(n):
    y = 0
    x = int(input())
    while x > 0:
        if x % 10 > y:
            y = x % 10
        x //= 10
    num += str(y)
print(num)