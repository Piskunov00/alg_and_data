# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает
# свои границы диапазона. Например, если надо получить случайный
# символ от 'a' до 'f', то вводятся эти символы. Программа должна
# вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# https://drive.google.com/file/d/1JKPNcPmVgnJNJJtn5W6tVZZd1ay5mlZe/view?usp=sharing

import random

a, b = map(int, input('Введите границы для 1 случая\n').split())
c, d = map(float, input('Введите границы для 2 случая\n').split())
e, f = map(str, input('Введите границы для 3 случая\n').split())
print('Вот ваши случайные значения:')
print(random.randint(a, b))
print(random.uniform(c, d))
print(chr(random.randint(ord(e[0]), ord(f[0]))))
