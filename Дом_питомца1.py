class Client:
    def __init__(self,firts_name,last_name,city,balance):
        self.first_name = firts_name
        self.last_name = last_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return (f'"{self.first_name} {self.last_name}. {self.city}.'
                f'Баланс: {self.balance}руб."')
    def only(self):
        return f'{self.first_name} {self.last_name},г.{self.city}'
