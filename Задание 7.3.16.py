text = input("Введите какой нибудь текст:")
last = text[0]
count = 0
result = ''

for c in text:
    if c == last:
        count += 1
    else:
        result += last + str(count)
        last = c
        count = 1
result += last + str(count)
print(result)