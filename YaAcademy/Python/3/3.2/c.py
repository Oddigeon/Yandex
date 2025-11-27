# Зайка — 8

# result = set()
# for i in range(int(input())):
#     text = input().split()
#     for t in text:
#         result.add(t)

# for r in result:
#     print(r)

result = set()
for _ in range(int(input())):
    result = result | set(input().split())
print('\n'.join(result))