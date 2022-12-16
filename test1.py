#   # a = 45 
# # b = 35
# # c = 55
# # d = a % b 
# # print(d)

# # a = int (input("a: "))
# # b = int (input("b: "))
# # print(b-2-a)
# # print(b+2-a)

#   # a = int (input("1: "))
# # b = int (input("2: "))
# # c = int (input("3: "))
# # print(a*b*c)


#   # a = int (input("First: "))
# # b = int (input("Second: "))
# # c = int (input("Third: "))
# # d = int(input("Four: "))
# # e = int(input("Five: "))
# # f = int (input("Six: "))
# # print (a*b*c*d*e*f)


#   # d = int(input("a: "))
# # p = d*4
# # s = d*2
# # print(p)


# # a = 5
# # c = 4
# # d=a
# # a=c
# # c=d

# aper = input('+ * : / % ')

# num1 = (input( ))
# num2 = int(input( ))
# if aper == '*':
#   print(f'{num1}{aper}{num2}=',num1*num2)

# elif aper =='+':
#   print(f'{num1}{aper}{num2}=',num1+num2)

# elif aper =='/':
#   print(f'{num1}{aper}{num2}=',num1/num2)

# elif aper =='%':
#   print(f'{num1}{aper}{num2}=',num1%num2)
# else:
#   print("???")


# text = input('napishi text s probelom: ')
# oper = input('* + ')
# num = int(input())

# if ' ' in text:
#   if oper == '*':
#     print(text * num)
#   else:
#     print('===')
# else:
#     print('V nem net probela')



# print('''КНБ
# 1.Rock
# 2.Paper
# 3.Sci
# ''')
# user1 = int(input("1Выберите номер: "))
# user2 = int(input("2Выберите номер: "))


# if user1 == user2:
#   print("Tie")
# elif user1 == 1 and user2 == 2:
#   print("User 2 win")
# elif user1 == 1 and user2 == 3:
#   print("User 1 win")
# elif user1 == 2 and user2 == 1:
#  print("User 1 win")
# elif user1 == 2 and user2 == 3:
#   print("User 1 win")
# elif user1 == 3 and user2 == 1:
#   print("User 2 win")
# elif user1 == 3 and user2 == 2:
#   print("User 1 win")
# else:
#   print("False")


# name = input('Введите имя: ')

# print(name.title()) #Все начальные буквы в верхнем регистре
# print(name.upper()) #Все буквы в верхнем регистре
# print(name.lower()) #Все буквы в нижний регистер
# print(name.swapcase()) #Все маленькие буквы большие и все большие в маленькие 
# print(name.capitalize()) #Начальные букву в верхниий регистер

# a = '5555'
# print(a.isdigit()) #Все ли состоит из цифр
# print(a.isalpha()) #Все ли состоит из букв
# print(a.isidentifier()) #Все ли у нас пишется слитно
# print(a.islower()) #Все ли у нас в нижнем регистре
# print(a.isupper()) #Все ли у нас в верхнем регистре
# print(a.istitle()) #Все ли у нас начинаются в большой буквы
# print(a.isnumeric()) #Все ли у нас состоит из цифр
# print(a.isspace()) #Все ли у нас в тексте состоит из пробелов
# print(a.isprintable()) #Все ли мы можем принтовать


# text = '1Privet welcome1'
# print(text.strip('1')) #Удаление начальной буквы
# print(text.rstrip('1')) #Удаление последнюю буквы
# print(text.lstrip('1')) #Удаления начальной буквы


# text = 'salom'
# print(text.center(9,'*')) #Выравнивание строки
# print(text.rjust(9,'*')) #Выравние строки с права
# print(text.ljust(9,'*')) #Выравнивание строки с лева

# print(text.zfill(10)) #Дополнение текста на 0
# print(f'salom{text}')
# print("salam {0} {1}".format('Hello','Bratan'))



# text = 'pgygthon, go,   cgg++'
# print(text.replace('c++', 'python')) #Замена подстроки в строке


# print(text.find('g',)) #Показать индекс буквы
# print(text.find('g',9)) #Показать индекс буквы после 3 индекса
# print(text.rfind('g',9))

# print(text.index('g',4))
# print(text.rindex('g',4))

# print('|*|'.join(text)) #Вернуть текст после каждой буквы *


# print(text.count('o',5)) #Сколько в тексте букв после 5го индекса
# print(text.count('o')) #Сколько в тексте букв

# print(text.split()) #Разделит наш текст и обернет его в массив
# print(text.splitlines()) #Весь текст обернет в массив

# print(text.partition('H')) #Разделить подстроу Hello от строки

# print(text.startswith('H')) #Начинается текст ли с буквы H
# print(text.endswith('d')) #Заканчивается ли наш текст с буквы d

# print(len(text)) #Подсчитает весь текст


# text = 'Hello'
# print(text[1:3])



# Напишите валидатцию пароля:
#       1. Запросим пароль и ее повторный ввод и проверить если они не совпадают сообщить об этом
#       2. Проверить пароль должен быть больше 8 символов
#       3. Проверить если в пароле есть '123' то сообщить 'Простой пароль'
#       4. После проверок добавить '|*|' после каждого символа в пароле

#   Создать предложение где одна его половина написана в маленьком регистре, 
#   а вторая полностью в большом.

#   Спросить у пользователя имя, возраст и любимый фильм.
#       Поприветствовать по имени.
#       Похвалить его фильм.

#   Спросить у прользователя имя и после каждого символа проставить символ '|'

#   Взять строку и заменить все буквы ч на число 4.


# a = 'HelloWorld'
# print(a[:5].lower(),a[5:].upper())

# user = input('Login: ')
# p1 = input('Your password:')
# if print(user.lower(),user.isaplha('')):
#     if len(p1) >= 8:
#         if '123' not in p1:
#             password = p1
#             print('Входите')
#             print('|*|'.join(password))
#             print(p1)            
#         else:
#             print('Ваш пороль должен быть больше 8 символов')
#     else:
#         print('Your password so ez')
# else:
#     print('Вы авторизованы')




# log = input('login: ')
# pas = input('Password: ')
# if len (pas) >= 8:
#     if pas in 'qwertyuiopasdfghjklzxcvbnm':
#         if pas.find(log):
#             print('True')
#         else:
#              print('False')
#     else:
#         print('Yes')
# else:
#     print('No')

    
# a = ('Hello',78,2.31,True,False,'QWERTYU')

# list1 = ['Hello',78,2.31,True,False,'QWERTYU']
# print(list1)
# list2 = list()
# list3 = []
# ERROR tuple1 = ()
# print (tuple1)
# print(type(tuple1))
# print(len(list1)-1)
# print(list1[])
# index=[0]

#slice срезы
#[:star[0]:stop[end]:step[1]] sss
# print(list1[2::-1])

# user1 = input('input word:')
# if user1 == user1 [:: -1]:
#     print(True)
# else:
#     print(False)

#print len type input
#var.method()
# list1 = ['Hello','world','Astana',False]
#append добавляет в конце элемент
# list1.append(True)
# list1.append('QWert')
# print(list1)
# #remove
# list1.remove(False)
# print(list1)

#extend


#list1.extend('Hello')
#print (list1)

# list1.pop(0)
# print(list1)


# print (list1.count(False))
# print(list1)



# print(list1.index())

# print(list1.clear)

# print(list1.reverse())



# import timeit
# list_test = [123,564,8645,6853,5312,321,6554,688498]
# list_test = timeit.timeit(stmt="(1,2,3,4,5)",number=1000)
# print(list_test)

# list_test1 = timeit.timeit(stmt="[1,2,3,4,5]",number=1000)
# print(list_test1z


#   Пользователь вводит имя файла. Проверить, находится ли расширение файла в списке допустимых.




# list1 = input("File name: ")
# list2 = ['png', 'jpg', 'jpeg', 'gif', 'svg']
# if "." in list1:
#     if list1.split('.')[1] in list2:
#         print(True)
#     else:
#         print(False)
# else:
#     print("net tochki")



# spisok = []
# spisok.append(('qwe'))
# spisok.append(('Life'))
# spisok.append(("no"))
# spisok.append(("life"))
# spisok.append((":DDD"))
# print(spisok)

# list1 = ['Hello','Close','Open']
# print(list1.index('Hello'))

# print(list1[0],list1[1],list1[2])
# print(list1)



# list1 = ['Alex','Stive','Miras','Bob']
# a = ','.join(list1)
# print(a.replace(',',' '))


# list2 = ['Shop','Magazine','Miras','Bob']
# a = ','.join(list2)
# print(a.replace(',',' '))



# list1 = ['Alex','Oskar']
# list1.remove('Oskar')
# print (list1)



# list1 = []
# list1.append(('Stas'))
# list1.append(('5.05.2007'))
# list1.append(('Python'))
# print (list1)

# f = dict()

# megi = {
#     'name': 'Ablay',
#     'age': 42
# }


# print (megi.get('e',0))
# a, b = megi.items()
# print (a,b)
# print (megi['name'],megi['age'])
# print (megi.get('name'),megi.get('age'))

# print (megi.items())
# print (megi.keys())
# print (megi.values())


# megi.pop('name')
# print (megi)


# megi.popitem()
# print(megi)

# megi.clear()
# print (megi)


# t = {
#     'last_name': 'baz'
# } 
# megi.update(t)


# megi.update()
# print(megi)

# print(megi.fromkeys('asd',[123]))

# a = megi.fromkeys('asd',[])

# a ['a'] = 10
# a ['b'].append(12)
# print(a)


# a = {'x':4, 'y':5}
# m.setdefault('z',123)
# print(m)


# b = a.copy()
# b["123"] = 123
# print(b)
# print(a)



# a = {'name' , 123, 321, 'name', True , False}
# a = list(a)
# print(list(a))
# print (type(a))

# b = frozenset([1,2,3,4])
# print(b)



# a = {'name' , 123, 321, 'name', True , False}
# b = {'name' , 123, 321, 'asd','asds', True , 2.123}
# c = {'1', '13'}
# print (c.isdisjoint(a))
# print (b.isdisjoint(a))

# print(a.union(b))
# print(a | b)


# print(a.intersection(b))
# print(a & b)
# print(a.difference(b))
# print(a - b)
# print(b - a)

# a.symmetric_difference(b))

# a.update(b)
# a.add(123123123)
# a.discard(123)
# print (a)


# a = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# a.discard(7)
# print (a)

# a = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}
# b = {1,2,3,4,5,6,7,8,9,10}
# c = {1,2,3,4,5}
# print (a.intersection(b))
# print (a.intersection(c))



# a = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# b = {1,2,3,4,5,6,7,8,9,10}
# c = {1,2,3,4,5}

# print (a.difference(b))
# print (a.difference(c))


# a = {1,2,3,4,5}
# a.add (6)
# b = a.pop()
# print(a)



# a = {
#     'lagman':130,
#     'borsh':130
# }

# a['besh_barmak'] = 130
# print(a)
# a['lagman'] = 135
# a.pop('borsh')
# print(a)



# a = {
#     'drinks': ('Coca-Cola','Sprite','Fanta')
# }
# print (a)



# a = {'True','False','ads',1,2,3,123}
# b = {
#     'add':'Добавляет элемент в множетсво',
#     'remove':'Удаляет объект из множества',
#     'clear': 'Удаляет всё внутри множетсва.',
#     'update': 'Добавляет в множетсво всё что вы передали в UPDATE()',
#     'difference': 'Сравнивает оригинальное множество с * и возвращает объекты которых нет в *',
#     'discard': 'Удаляет * из множетсва, если * нету во множестве, ошибки не будет как если бы это было remove()',
#     'intersection': 'Возрвращает объекты которые есть и во множестве и в *.',
#     'intersection_update': 'Удаляет из множетсва непохожие и оставляет только те объекты которые есть и во множестве и в *',
#     'pop': 'Удаляет рандомный объект из множества.'
# }
# print(a)
# print(b['add'])



# baza = {
#     'login': {
#         'password': '5256',
#         'name': 'stas',
#         'data_birth': '05.05.2007',
#     }
# }



#loop for start stop step
#int not item objet

# string = 'Hello'
# for i in range(100):
#     print(i)



# list = [1,2,3,4,5,6]
# dict1 = {
#     "name" : "Admin",
#     "pos" : "superuser",
#     "id" : 1
# }
# for i in dict1['name']:
#     print (i)


# i = 1000
# while i>1:
#     i-=10     #i = i -10     i+=5    i = i + 5 i/=5   i = i / 5
#     print(i)


# i = 1000
# while i>= 0:
#     print('Hello')
#     print(i)



# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# list2 = []
# list3 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
#     else:
#         list3.append(i)
# print(list2)
# print(list3)


# i = 10
# while i!=0:
#     i-=1
#     print (i)
#     if i ==5 :
#         break



# list6 = [1,2,3,45,6,7,789]
# for item in list6:
#     if item==7:
#         print(item)
#         break
#     else:
#         continue



# list6 = ['hi','my','name','is','shelbi']
# for item in list6:
#     print(item, end='')  #\n



# for i in range(5):
#     print('*', end= '')
#     for j in range(4):
#         print('*', end= '')
#         for k in range(3):
#             print('*', end= '')
#             for q in range(2):
#                 print('*', end= '')



# list1 = ['apple','banana','cherry']
# for i in range(6):
#     a = input("input fruits")
#     list1.append(a)
# print(list1)
# while list1 ==5:



# i = 1000
# while True:
#     i -=7
#     print('pair')
#     if i <= 0:
#         print('olive')
#         break


# count = 0
# while count<4:
#     count<=1
#     print('Hello python')
# else:
#     print("Helo java")





# while True:
#     aper = input('+ * : / % ')
#     num1 = int(input("Введите число 1: "))
#     num2 = int(input("Введите число 2: "))
#     if aper == '*':
#       print(f'{num1}{aper}{num2}=',num1*num2)

#     elif aper =='+':
#        print(f'{num1}{aper}{num2}=',num1+num2)

#     elif aper =='/':
#         print(f'{num1}{aper}{num2}=',num1/num2)

#     elif aper =='%':
#         print(f'{num1}{aper}{num2}=',num1%num2)
#     else:
#         print("Error")




# for i in range(10):
#     for j in range(i):
#         print ('#',end='')
#     print(' ')


# for i in range(1):
#     print("*".rjust(3, " "))
#     for j in range(1):
#         print("***".center(5, " "))
#     for k in range(1):
#         print("*".center(5, "*"))
#     for q in range(1):
#         print("***".center(5, " "))
#     for l in range(1):
#         print("*".rjust(3, " "))



# n = 5
# z = '*'
# a = n * len(z) * 2 
# for i in range(1,n*2+1,2):
#     print(f'{z*i}'.center(a))
# for i in range(n*2-3,0,-2) :
#     print(f'{z*i}'.center(a))





# baza = {
#     'Baiden' : {
#         'phone' : '+77717777777',
#         'name' : 'Joe',
#         'balance' : '100000',
#         'password' : 'baidenkeys'
#     },
#     'hiro' : {
#         'phone' : '+87725228909',
#         'name' : 'hiro',
#         'balance' : '99999',
#         'password' : 'hironotbaiden',
#     }
# }

# key = None

# while True:
#     if key is not None:
#         print(f' Здравствуйте {key}')


#     table = int(input("""
#       1 >>> Регистрация
#       2 >>> Авторизация
#       3 >>> Перевод баланса
#       4 >>> Список пользователей
#       5 >>> Информация
#       6 >>> Номер телефона
#       7 >>> Выход
#       """))


#     if table == 1:
#         if key is None:
#             login = input ("Напиши ваш логин: >>> ")
#             if login.isalpha():
#                 name = input("Напиши твое имя: >>> ")
#                 if login.isalpha():
#                     phone = input("Напиши свой номер телефона +7 >>> ")
#                     if phone.isdigit():
#                         password = input('Напиши свой пароль: ')
#                         password2 = input('Повтори свой пароль:')
#                         while password != password2 or password or len(password) < 8:
#                             password = input ('Напиши свой пароль: ')
#                             password2 = input('Повтори свой пароль: ')
#                         else:
#                             baza.update ({
#                                 login : {
#                                     'name' : 'name',
#                                     'phone' : 'phone_number',
#                                     'balance' : '100',
#                                     'password' : 'password2'
#                                 }
#                             })
#                             key = login
#                     else:
#                         print('Номер должен состоять только из цифр')
#                 else:
#                  print('Имя должно быть только из букв')
#             else:
#                 print('Логин долден быть только из букв')
#         else:
#             print('Вы уже зарегестрированы')


#     elif table == 2:
#         if key is None:
#             login = input('Напиши свой логин: ')
#             if login in baza.keys():
#                 password = input('Напиши свой пароль: ')
#                 if password == baza[login]['password']:
#                     print('Вы авторизовались')
#                     key = login
#                 else:
#                     print('У вас не верный пароль')
#             else:
#                 print('В базе нет такого пользователя')
#         else:
#             print('Вы уже авторизованы')


#     elif table == 3:
#         if key is not None:
#             login_komu = input('Введите логин получателя')
#             if login_komu.isalpha() and login_komu in baza.keys():
#                 summa = int(input("Введите сумму перевода: "))
#                 if summa <= baza[login]['balance']:
#                     baza[login]['balance'] -= summa
#                     baza[login_komu] += summa
#                     print('Перевод выполнен')
#                 else:
#                     print('У вас не хватает средств для перевода')
#             else:
#                 print('Не верно указан логин или не найден пользователь')
#         else:
#             print('Сначало авторизуйся')


#     elif table == 4:
#         if key is not None:
#             print(baza)
#         else:
#             print('Сначало авторизуйся')
    

#     elif table == 5:
#         if key is not None:
#             print(f'''
#             Ваши данные
            
#             login: {key}
#             name: {baza[login]['name']}
#             balance: {baza[login]['balance']}
#             password: {baza[login]['password']}

#             ''')
#         else:
#             print('Сначало авторизуйся')
#     elif table == 6:
#         if key is not None:
#             print(f'phone number +7{baza[login]["phone"]}')
#         else:
#             print('Сначало авторизуйся')

#     elif table == 7:
#         key = None
#         print('Вы вышли из аккаунта')


#1

# a = [1, 1, 2, 3, 5, 8, 13, 12, 34, 55, 89]
# for i in a:
#     if i <= 13:
#         print(i,end= '')



#2

# list1 = [1, 2, 3, 4, 5, 8, 13, 12, 34, 55, 89]
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# list3 = []
# for i in list1:
#     if i in list2:
#         list3.append(i)    
# print(list3)
    

 
#4
# baza = {
#     'Kapysta' : {
#         'name' : 'Joe' ,
#         'login' : 'Baiden'
#     }
# }

# baza2 = {
#     'Kartofan' : {
#         'name' : 'Karto',
#         'login' : 'Fun'
#     }
# }

# baza.update(baza2)
# print(baza)

#5

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# for i in my_dict.values():
#     if i >=560:
#         print(i)


#6
# print(int('ABC',16))


#8
# list1 = (input())








#9
# n = int(input())
# hours = (n // 3600) % 24
# n = n % 3600
# minutes = n // 60
# n = n % 60
# sec = n
# print(hours, str(minutes // 10) + str(minutes % 10), str(sec // 10) + str(sec % 10), sep=':')




 #10









 #11
# list1 = ['avacado','persik','qiwi','banan']

# print(list1)







#13
# n = 305
# n2 = n * 2
# n3 = n * 3

# print(n + n2 + n3)

#14
# ch = []
# nch = []
# n = [1,2,3,4,5,6,7,8,9,10,11,12,240]

# for i in n:
#     if i % 2 == 0:
#         ch.append(i)
#     elif i == 237:
#         break
# print()