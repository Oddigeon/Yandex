sum = 0
while (price := float(input())) != 0:
    if price >= 500:
        price = price - (price // 10)
    sum = sum + price
print(sum)