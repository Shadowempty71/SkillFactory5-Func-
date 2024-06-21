# Yапишите функцию, которая проверяет,
# является ли данная строка палиндромом или нет,
# и возвращает результат проверки. Пример:
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True
def check_palindrome(text):
    text = text.lower()
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    if text == text[::-1]:
        return True
    else:
        return False
text = "Кит на море не романтик"
print(check_palindrome(text))