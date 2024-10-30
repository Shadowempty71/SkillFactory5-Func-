from Дом_питомца1 import Client

cl_1 = Client("Михаил","Ваганов","Москва",1000000)
cl_2 = Client("Андрей","Орлов","Тула",10000000)
cl_3 = Client("Василий","Филатов","Тула",5000000)

clients = [cl_1,cl_2,cl_3]

for client in clients:
    print(client.only())