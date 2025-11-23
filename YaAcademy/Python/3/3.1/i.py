# Без комментариев

while phrase := input():
    if phrase.startswith('#'):
        continue
    elif phrase.find('#') != -1:
        print(phrase[:phrase.find('#')])
    else:
        print(phrase)
