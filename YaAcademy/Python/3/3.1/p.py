# Анонс новости 2.0

limit = int(input())
texts = []

for _ in range(int(input())):
    texts.append(input())
if len("".join(texts)) <= limit:
    print("\n".join(texts))
else:
    limit -= 3
    for text in texts:
        if len(text) < limit:
            print(text)
            limit -= len(text)
        else:
            print(text[:limit] + "...")
            break