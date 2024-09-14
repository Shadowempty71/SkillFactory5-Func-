def create_user(**kwargs):
    '''Создает словарь с данными нового пользователя'''
    new_dict = {}
    for enumerate in kwargs.items():
        new_dict.update(kwargs)
    return new_dict
user = create_user(surname = 'Сидоров', name = 'Петр', patronymic = 'Иванович', age = 30, email = 'john@example.com')
print(user)
# Задача со звёздочкой: Объеденить параметры "Фамилия","Имя" и "Отчество" в один параметр