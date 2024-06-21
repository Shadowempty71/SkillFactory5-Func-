def char_frequency(text):
    for i in [" ", "\n"]:
        text = text.replace(i, "").lower()

    count = {}
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char, cnt in count.items():
        print(f"Символ {char} встречается {cnt} раз")


input_text = input("Введите любой текст: ")
char_frequency(input_text)