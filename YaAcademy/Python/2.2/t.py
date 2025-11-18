x1 = input()
x2 = input()
x3 = input()
pat = ''

if 'зайка' in x1:
    pat = x1
if 'зайка' in x2:
    if pat == '' or pat > x2:
        pat = x2
if 'зайка' in x3:
    if pat == '' or pat > x3:
        pat = x3

print(pat, len(pat))