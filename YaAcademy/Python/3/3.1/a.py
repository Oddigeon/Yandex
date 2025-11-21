#   Азбука

n = int(input())
count = 0
for _ in range(n):
    word = input()
    if word[0] in 'абв':
        count += 1

if count == n:
    print('YES')
else:
    print('NO')