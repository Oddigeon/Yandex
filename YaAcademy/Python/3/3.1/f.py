n = int(input())
count = 0

for i in range(n):
    phrase = input()
    count += phrase.count('зайка')

print(count)