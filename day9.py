# a = ['Stat\n','Mars\n','Miras']
# file = open ('Itcbootcamp.py', 'a+')
# file.write('Hello World\n')
# file.write('Hello Mars\n')
# file.writelines(a)
# file.close()



# f =open('Itcbootcamp.txt', 'r')
# a = f.read()
# b = f.readline() #Прочитает указанную строку
# c = f.readlines() #Прочитает файл полсностью
# print(a)
# f.close()



# a = open('w')
# a.write()
# a.close
# with open('w') as f:
#     f.write()

# login = input('Write your login: ')
# password = input('Write your password: ')

# with open('users.txt', 'a+') as f:
#     f.write(f'{login}, {password}')


# with open('users.txt','r') as f:
#     a = f.readline()
# print(a)
# for i in a:
#     if i == 'w':
#         print('Yes')
#     else:
#         print('No')


# t_work = []
# with open('python.txt','w') as f:
#     f.write('''
#     zawxescdrvf tbgyhnumijqz wxecr vtybunimk jhgfdsauytiusty 
#     DGDRGDRUGUGSUUYETES OFES ZWXECYTFVGBHNJMK YVYRDYZ
#     ''')
# with open('python.txt','r') as a:
#     python = a.read()
#     for i in python.split():
#         for j in i:
#             if j == 't' or j == 'T':
#                 t_work.append(i)
# print(t_work)


# login = input('login: ')
# password = input('password: ')
# with open('database.txt','w') as f:
#     f.write(f'{login},{password}')

# with open('database.txt','r') as r:
#     lp = r.readlines()
#     print(lp)

# while True:
#     table = int(input("""
#        1 >>> Регистрация
#        2 >>> Авторизация
#     """))
#     if table == 1:
#             login = input ("Напиши ваш логин: >>> ")
#             password = input('Напиши свой пароль >>> ')
#             password2 = input('Повтори свой пароль >>> ')
#             while password !=password2:
#                 print('Пароли должны быть одинаковыми')
#                 password = input('Введите пароль повторно')
#                 password2 = input('Введите пароль еще раз')
#             else:
#                 with open('database.txt', 'r') as f:
#                     database = f.readlines()
#                     for i in database:
#                         if i == f'{login}, {password}':
#                             print('Такой пользователь уже есть')
#                         else:
#                             with open ('database.txt', 'r') as new_database:
#                                 new_database.write(f'{login}, {password}')
#                             print('Вы успешно зарегестированы')


# a = ['Alibek\n','Guluzim\n','Adi\n','Miraz\n','Stas\n','Darhan\n','Salamon\n','Roman\n']
# with open('ItcBoot.txt', 'a+') as f:
#     f.writelines(a)
#     f.write('Hello Itc-Bootcamp\n')
