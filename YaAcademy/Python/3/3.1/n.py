# Массовое возведение в степень 2.0

nums = input().split()
degree = int(input())
result = []

for num in nums:
    result.append(str(int(num) ** degree))
print(' '.join(result))