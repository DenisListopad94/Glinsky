'''

1. Напишите функцию fib, которая будет выводить последовательно каждое число Фиббоначи
'''

# def fib_generator():
#     a, b = 0, 1
#
#     def fib():
#         nonlocal a, b
#         result = a
#         a, b = b, a + b
#         return result
#
#     return fib
#
# # Создаем генератор
# fib_func = fib_generator()
#
# print(fib_func())
# print(fib_func())
# print(fib_func())
# print(fib_func())
# print(fib_func())
# print(fib_func())
# print(fib_func())

'''
2.	Напишите функцию simple, которая будет выводить поочерёдно простые числа от 2 до введённого числа n до вызова исключения.
'''
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def simple_generator(n):
#     current_number = 2
#
#     def simple():
#         nonlocal current_number
#         while current_number <= n:
#             if is_prime(current_number):
#                 result = current_number
#                 current_number += 1
#                 return result
#             current_number += 1
#         raise StopIteration("No more prime numbers")
#
#     return simple
#
# # Создаем генератор
# simple_func = simple_generator(20)
#
# # Печатаем простые числа до вызова исключения
# try:
#     while True:
#         print(simple_func(), end=" ")
# except StopIteration as e:
#     pass

'''
3.	Напишите генератор для вывода всех совершенных чисел до 1000000000
'''
# def is_perfect(num):
#     divisors_sum = sum(divisor for divisor in range(1, num) if num % divisor == 0)
#     return divisors_sum == num
#
# def perfect_number_generator():
#     current_number = 2
#
#     while True:
#         if is_perfect(current_number):
#             yield current_number
#         current_number += 1
#
# # Создаем генератор
# perfect_gen = perfect_number_generator()
#
# # Выводим все совершенные числа до 1000000000
# try:
#     while True:
#         print(next(perfect_gen), end=" ")
# except StopIteration as e:
#     pass
#

''' 
4.	Исключить из строки группы символов, расположенные между первыми символами '{' и '}' 
вместе со скобками. Если нет символа '}', то исключить все символы до конца строки после '{'.  
Вывести символ, наиболее часто встречающийся в строке.
'''

# from collections import Counter
#
# def process_string(input_str):
#     # Ищем индекс первого '{' и '{' последующего за ним
#     opening_brace_index = input_str.find('{')
#     closing_brace_index = input_str.find('}', opening_brace_index)
#
#     # Если найдены оба символа '{' и '}'
#     if opening_brace_index != -1 and closing_brace_index != -1:
#         processed_str = input_str[:opening_brace_index] + input_str[closing_brace_index + 1:]
#     # Если найден только символ '{'
#     elif opening_brace_index != -1:
#         processed_str = input_str[:opening_brace_index]
#     # Если не найдены оба символа
#     else:
#         processed_str = input_str
#
#     # Убираем пробелы и находим наиболее часто встречающийся символ
#     processed_str_without_spaces = processed_str.replace(" ", "")
#     most_common_char = max(Counter(processed_str_without_spaces).items(), key=lambda x: x[1], default=(" ", 0))[0]
#
#     return processed_str, most_common_char
#
# # Пример использования
# input_string = "This is {a sample} string with {some text} and more."
# result, most_common_character = process_string(input_string)
#
# print("Processed String:", result)
# print("Most Common Character:", most_common_character)

'''
5.	Ваш отдел работает над приложением, обращающимся к некоторому серверу. Вам поручили реализовать некоторые запросы: GET, POST и DELETE. В контексте вашего приложения POST-запрос добавляет строку на сервер, GET-запрос возвращает последнюю добавленную строку, а DELETE-запрос удаляет последнюю добавленную строку. Дан список команд с запросами (GET и DELETE не принимают параметров, а POST принимает строку или число), список команд прерывается точкой. Выведите, что возвращает сервер, а также строки, которые остались в списке, разделяя их через пробел.
Sample Input:
POST 12
POST 15
POST 81
GET
DELETE
DELETE
POST Stack Overflow
POST Recursion
DELETE
GET
.
Sample Output:
81
              Stack Overflow

'''
# class Server:
#     def __init__(self):
#         self.data = []
#
#     def process_request(self, command):
#         if command.startswith("POST"):
#             parts = command.split(maxsplit=1)
#             if len(parts) > 1:
#                 value = parts[1]
#                 self.data.append(value)
#                 return None
#             else:
#                 return "Invalid POST command"
#         elif command == "GET":
#             return self.data[-1] if self.data else "None"
#         elif command == "DELETE":
#             if self.data:
#                 deleted_value = self.data.pop()
#                 return None
#             else:
#                 return "None"
#         else:
#             return "Invalid command"
#
# # Создаем объект сервера
# server = Server()
#
# # Считываем команды
# commands = []
# while True:
#     command = input().strip()
#     if command == ".":
#         break
#     commands.append(command)
#
# # Обрабатываем команды
# for command in commands:
#     result = server.process_request(command)
#     if result is not None:
#         print(result)

'''Реши задачу на Python:
6.	Используя list comprehension. Сгенерируйте список как показано ниже:

1 1 1 1 1 1  
1 2 3 4 5 6
1 3 6 10 15 21
1 4 10 20 35 56
1 6 21 56 126 252

'''




'''
7.	Коля понял, что у многих из его знакомых есть несколько телефонных номеров и нельзя хранить только один из них. 
Он попросил доработать Вашу программу так, чтобы можно было добавлять к существующему контакту новый номер или даже 
несколько номеров, которые передаются через запятую.
'''
# class Contact:
#     def __init__(self, name, phones=None):
#         self.name = name
#         self.phones = phones or []
#
#     def add_phone(self, new_phones):
#         # Разбиваем строку с новыми номерами по запятой
#         new_phones_list = new_phones.split(',')
#         # Добавляем новые номера к списку телефонов контакта
#         self.phones.extend(new_phones_list)
#
#     def __str__(self):
#         return f'{self.name}: {", ".join(self.phones)}'
#
# # Пример использования
# contacts = []
#
# # Создаем контакт
# contact1 = Contact('John', ['123456789'])
# contacts.append(contact1)
#
# # Добавляем новые номера к существующему контакту
# contact1.add_phone('987654321,111222333')
#
# # Выводим информацию о контактах
# for contact in contacts:
#     print(contact)
