# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')


# get_password - функция для создания пароля
def get_password(number):
    return int(''.join([str(i) + str(j)
                        if not number % (i + j) and i < j else ''
                        for i in range(1, number)
                        for j in range(2, number)]))


# Сгенерируем пароль
print('\nВВОД ДАННЫХ\n')
n = ''

while not n.isnumeric():
    n = input('Введите число от 3 до 20: ')

    if n.isnumeric():
        if 3 <= int(n) <= 20:
            n = int(n)
            break
        else:
            n = ''

# Выведем пароль
print('\nВЫВОД ДАННЫХ')
print('\nПароль:', get_password(n), end='.\n\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
