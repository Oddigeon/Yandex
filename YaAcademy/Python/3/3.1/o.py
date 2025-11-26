# НОД 3.0

nums = input().split()
a = int(nums[0])
for num in nums[1:]:
    b = int(num)
    while b:
        a, b = b, a % b
print(a)
    