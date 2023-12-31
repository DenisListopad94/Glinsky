'''
1.	Напишите функцию которая будет генерировать список из 10 чисел степени 2 от 1 до 10.
'''
# def numbersInPower():
#     print([i**2 for i in range(1,11)])
# numbersInPower()
'''
2.	Напишите функцию которая будет генерировать список всех трёхзначных чисел кратных 5 и 3.
'''
# def generatorListOfDigits():
#     print([i for i in range(100,1000) if i % 3 == 0 and i % 5 == 0])
# generatorListOfDigits()

'''
3.	Программа получает на вход три числа через пробел — начало и конец диапазона, а также степень, 
в которую нужно возвести каждое число из диапазона. Напишите функцию которая сгенерирует и вернёт данный.

Sample Input:
5 12 3
Sample Output:
125 216 343 512 729 1000 1331 1728
'''

# def generOfListsSpecifiedByRangeAndPower():
#     s = input().split()
#     print([i**int(s[-1]) for i in range(int(s[0]),int(s[1]))])
# generOfListsSpecifiedByRangeAndPower()

'''
4.	Напишите функцию, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого 
списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", 
то на выход ожидается список "13 6 9 15 7" (без кавычек).Если на вход пришло только одно число, надо вывести его же. 
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:
1 3 5 6 10
Sample Output 1:
13 6 9 15 7
Sample Input 2:
10
Sample Output 2:
10
'''

# def sumNeighbors(*args):
#     list = []
#     if len(args) == 1:
#         print(*args)
#
#     elif len(args) == 2:
#         list.append(args[0] + args[1])
#         list.append(args[0] + args[1])
#         print(*list)
#
#     elif len(args) > 2:
#         list.append(args[-1] + args[1])
#         [list.append(args[i - 1] + args[i + 1]) for i in range(1, len(args) - 1)]
#         list.append(args[-2] + args[0])
#         print(*list)
#
#     else:
#         print('Function must contain at least 1 digit')
#
#
# sumNeighbors(2, 3, 4, 5, 6, 7, 8)

'''
5.	Напишите функцию, для нахождения минимального элемента из 2 чисел. 
С помощью данной функции найдите минимальное четырёх чисел.
'''

# def minFromTwo(var_1: int, var_2: int) -> int:
#     return var_1 if var_1 < var_2 else var_2
#
#
# min = minFromTwo(minFromTwo(10, 5), minFromTwo(4, 7))
#
# print(min)

'''
6.	Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), 
вычисляющую расстояние между точкой (x1, y1) и (x2, y2). Считайте четыре действительных числа и 
выведите результат работы этой функции.
'''

# def distance(x1: float, y1: float, x2: float, y2: float) -> tuple:
#     return abs(x1 - x2), abs(y1 - y2)
#
# print(distance(1, 1, 4, 5))

'''
7.	Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
Ищем число Фиббоначи через цикл! Рекурсию не использовать!
'''

# def fib(n):
#     prev = 0
#     curr = 1
#     for _ in range(n-2):
#         prev, curr = curr, prev + curr
#     print(curr)
#
# fib(10)


'''
8.	Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x 
и возвращающую самое маленькое целое число y, такое что:
-y больше или равно x
-y делится нацело на 5
10 - > 10
12,14,13 ->15
Попробуйте решить без цикла!
'''

# def closest_mod_5(x: int) -> int:
#     if x % 5 == 0:
#         return x
#
#     else:
#         return (x//5+1)*5
#
#
# print(closest_mod_5(12))


'''
9.	Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные 
значения, а чётные нацело делит на два. Функция не должна ничего возвращать, 
требуется только изменение переданного списка.
'''
# def modify_list(l):
#     l = [i for i in l if i % 2 == 0]
#
# modify_list([1,2,3,4,5,6,7,8,9])

'''
10.	*В языке Python есть некоторые ограничения на имена переменных. Имена переменных
-могут состоять только из цифр, букв и знаков подчеркивания.
-не могут начинаться с цифры.
Программист вводит строки с именами переменных. Для каждой переменной нужно вывести "Можно использовать", 
если ее имя корректно, или "Нельзя использовать", если это не так. Определив все нужные переменные, 
программист заканчивает ввод строкой "Поработали, и хватит".
Для проверки каждой строки используйте функцию check_variable(v). Для простоты будем считать, 
что программист использует только латинские буквы.
Не может содержать : ! @ # $ % ^ & * ()
'''

# def check_variable(v:str):
#
#     while True:
#         if v == "Поработали, и хватит":
#             break
#         elif (v[0] in '0 1 2 3 4 5 6 7 8 9 ! @ # $ % ^ & * () -'
#               or v.isdigit()
#               or v[0].isupper()):
#             print("Нельзя использовать")
#         else:
#             print("Можно использовать")
#         v = input()
#
# check_variable("smqwe")

'''
11.	*Сгенерировать список всех простых чисел до  100.
'''
# lst = []
# count = 0
# for i in range(1, 101):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         lst.append(i)
#     count = 0
# print(lst)

