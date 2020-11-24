'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = int(input('Введите номер сесяца: '))
if month in [1, 2, 12]:
    print('Зима')
elif month in [3, 4, 5]:
    print('Весна')
elif month in [6, 7, 8]:
    print('Лето')
elif month in [9, 10, 11]:
    print('Осень')


months = {
    1: 'Зима', 2: 'Зима', 12: 'Зима',
    3: 'Весна', 4: 'Весна', 5: 'Весна',
    6: 'Лето', 7: 'Лето', 8: 'Лето',
    9: 'Осень', 10: 'Осень', 11: 'Осень'
}
month = int(input('Введите номер сесяца: '))
# if month in months == 1 or 2 or 12:
#     print(months.get(1))
# elif month in months == 3 or 4 or 5:
#     print(months.get(3))
if month == 1 or 2 or 12:
    print(months.get(1))
elif month == 3 or 4 or 5:
    print(months.get(4))
elif month == 6 or 7 or 8:
    print(months.get(7))
elif month == 9 or 10 or 11:
    print(months.get(10))
