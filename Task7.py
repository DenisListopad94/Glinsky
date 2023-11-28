'''
1.	Создайте lambda-функцию для нахождения подстроки в введённой строке.
'''

# f = lambda str_nested, str_main: str_nested in str_main
# print(f('asd', 'qweqeqwasd'))

'''
2.	Проверьте число на чётность с помощью анонимной функции.
'''

# f = lambda nubmer: not nubmer % 2
# print(f(2))

'''
3.	Напишите lambda-функцию, которая будет приветствовать пользователя имя которого введено корректно, 
с большой буква. Иначе будет выводить сообщение о неверно введённом имени.
'''

# f = lambda name: print(f'Привет {name}' if str(name).istitle() else print("Неправильно введенное имя"))
# f("Вася")

'''
4.	Напишите рекурсивную функцию digits(n), которая принимает натуральное число и возвращает строку с 
цифрами этого числа справа налево, разделяя их пробелами.
Sample Input:
14623
Sample Output:
3 2 6 4 1
'''

# def number_reverse(number: int) -> str:
#     if number != 0:
#         print(number % 10, end=" ")
#         number_reverse(int(number // 10))
#
# number_reverse(12345)


'''
5.	Напишите рекурсивную функцию is_power(n), которая возвращает True, если переданное натуральное число 
является степенью двойки, и False иначе. 
Sample Input:
1048576
Sample Output:
True
'''

# def is_power(n):
#     n = n/2.0
#     if n == 2:
#         return True
#     elif n > 2:
#         return is_power(n)
#     else:
#         return False
#
# print(is_power(8))

'''
6.	Дано натуральное число N. Вычислите сумму его цифр
Sample Input:
14623
Sample Output:
16
'''


# def sum_of_digits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
# print(sum_of_digits(146))

'''
7.	Дана функция, которая выводит все простые числа в промежутке от 1 до 100. Написать декоратор который будет 
проверять время работы этой функции. Задекорировать функцию. Вывести вpемя работы этой функции, 
а так же сами простые числа.
'''
# import time
# def timing_decorator(func):
#     def inner(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Время выполнения функции {func.__name__}: {elapsed_time:.4f} секунд")
#         return result
#     return inner
#
# @timing_decorator
# def print_primes():
#     primes = []
#     for num in range(2, 101):
#         is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
#         if is_prime:
#             primes.append(num)
#     print("Простые числа:", primes)
#
# print_primes()

'''
8.	Дана функция, которая проверяет введённый пользователем пароль. Задекорировать её так, 
чтобы при правильно введённом пароле она приветствовала пользователя.
'''
# def greeting_decorator(func):
#     def inner(password):
#         result = func(password)
#         if result:
#             print("Добро пожаловать!")
#         return result
#     return inner
#
# @greeting_decorator
# def check_password(password):
#     # Предположим, что правильный пароль - "secret"
#     correct_password = "secret"
#     if password == correct_password:
#         print("Пароль верный.")
#         return True
#     else:
#         print("Неверный пароль.")
#         return False
#
# check_password('secret')
