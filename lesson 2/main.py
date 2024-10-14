from random import *

# Вводится строка. Определить является ли она палиндромом и вывести соответствующее сообщение.
s = input('Введите строку на проверку на палиндрома: ')
print('YES' if s[:] == s[::-1] else 'NO', '\n')

# В строке, состоящей из слов, разделенных пробелом, найти самое длинное слово.
print(max(input('Введите слова, разделенные пробелами, для поиска самого длинного слова: ').split(), key=len), '\n')

# # Генерируется список случайных целых чисел. Определить, сколько в нем четных чисел, а сколько нечетных.
numbers = [randint(1, 10000) for i in range(int(input('Введите количество целых чисел для генерации: ')))]
print(*numbers)  # вывод сгенерированных чисел
print('Количество четных чисел:', sum(1 for num in numbers if num % 2 == 0))  # сумма четных чисел
print('Количество нечетных чисел:', sum(1 for num in numbers if num % 2 != 0), '\n')  # сумма нечетных чисел

# Дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Заменить в строке все слова, входящие в словарь, как ключи, на их синонимы.
dct = dict(веселый='радостный', грустный='печальный', холодный='ледяной', синий='голубой')
s = 'веселый грустный холодный синий'.split(' ')
print(*s)
print(*[dct[s[i]] for i in range(len(s))], '\n')

# Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
# В этой задаче нельзя использовать циклы — используйте рекурсию.
def fib(num: int) -> int:
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


print('Фибоначчи:', fib(int(input('Введите целое неотрицательное число: '))), '\n')

# Сосчитайте количество строк, слов и букв в произвольном текстовом файле. (слова разделены пробелом, \n не считается символом)
with open('example.txt', 'r') as s:
    text = s.read()
    print(text)
print('Количество строк: ', text.count('\n'))
print('Количество слов: ', len(text.split()))
print('Количество букв: ', sum([1 for c in text if c.isalpha()]), '\n')

# Создайте генератор, выводящий бесконечную геометрическую прогрессию. Параметры прогрессии задаются через аргументы генератора
def geometric_progression(b, q):
    while True:
        b *= q
        yield b


f = geometric_progression(int(input("Введите первый член последовательности b: ")), int(input("Введите знаменатель q: ")))
for i in range(int(input("Введите, сколько первых членов последовательности нужно вывести: "))):
    print(next(f))