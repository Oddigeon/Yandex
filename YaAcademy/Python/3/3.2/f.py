# 1

# n, m = int(input()), int(input())
# result = set()
# ex = []

# for _ in range(n + m):
#     if (name := input()) not in result:
#         result.add(name)
#     else:
#         result.discard(name)

# if len(result) == 0:
#     print('Таких нет')
# else:
#     for res in result:
#         ex.append(res)
#     result = sorted(ex)
#     for res in result:
#         print(res)

#   ---------------------------------
# 2 

n, m = int(input()), int(input())
children = set()

for _ in range(n + m):
    if (child := input()) in children:
        children.discard(child)
    else:
        children.add(child)

if len(children) == 0:
    print('Таких нет')
else:
    print('\n'.join(sorted(children)))