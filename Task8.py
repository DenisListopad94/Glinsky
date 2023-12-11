'''

Задачи на файлы

1.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла
добавлен восклицательный знак.
'''
# with open('test.txt', 'r') as file:
#     for line in file:
#         if '!' in line:
#             print(line.rstrip())

'''
2.	Создать файл input.txt и записать в него 10 чисел через пробел. Считать из него эти числа.
Затем записать их произведение в файл output.txt.
'''

# with open('numb.txt', 'w') as file:
#     file.write(' '.join([str(i) for i in range(1,11)]))
# with open('numb.txt', 'r') as file, open('output.txt', 'w') as outputFile:
#     lst = [int(i) for i in file.readline().split()]
#     total = 1
#     for i in lst:
#         total *= int(i)
#     outputFile.write(str(total))

'''
3.	Список товаров, имеющихся на складе, включает в себя наименование товара, количество единиц товара,
цену единицы и дату поступления товара на склад. Вывести список товаров, хранящихся больше месяца и стоимость
которых превышает 1 000 000 р.
'''
#
# from datetime import date, timedelta
#
# def filter_expensive_and_old_products(products):
#     one_month_ago = date.today() - timedelta(days=30)
#
#     filtered_products = []
#
#     for product in products:
#         product_date = product['date']
#         days_difference = (date.today() - product_date).days
#
#         if days_difference > 30 and product['quantity'] * product['price_per_unit'] > 1000000:
#             filtered_products.append(product)
#
#     return filtered_products
#
# # Пример списка товаров
# products_list = [
#     {'name': 'Товар1', 'quantity': 100, 'price_per_unit': 12000, 'date': date(2023, 1, 1)},
#     {'name': 'Товар2', 'quantity': 50, 'price_per_unit': 30000, 'date': date(2023, 2, 15)},
#     {'name': 'Товар3', 'quantity': 200, 'price_per_unit': 5000, 'date': date(2022, 10, 1)},
# ]
#
# filtered_products = filter_expensive_and_old_products(products_list)
#
# # Выводим отфильтрованный список товаров
# for product in filtered_products:
#     print(f"Товар: {product['name']}, Количество: {product['quantity']}, "
#           f"Цена за единицу: {product['price_per_unit']}, Дата поступления: {product['date']}")
#

'''
4.	Создать словарь в качестве ключа которого будет 5-ти значное число, а в качестве значений кортеж состоящий
из 2-ух элементов – имя(str) и возраста(int). Сделать 5-6 элементов словаря и записать данный словарь на диск в
файл json формата
'''

# import json
#
# # Создаем словарь
# data_dict = {
#     12345: ('Иван', 25),
#     54321: ('Мария', 30),
#     98765: ('Алексей', 22),
#     67890: ('Екатерина', 28),
#     13579: ('Павел', 35)
# }
#
# # Записываем словарь в файл в формате JSON
# output_filename = 'data.json'
# try:
#     with open(output_filename, 'w') as file:
#         json.dump(data_dict, file)
#     print(f"Словарь записан в файл {output_filename}.")
# except Exception as e:
#     print(f"Произошла ошибка при записи в файл {output_filename}: {e}")


'''
5.	Прочитать сохранённый json – файл и записать данные на диск в csv файл. Первое значение каждой строки должно
начинаться со слова person, значения разделить ;
'''
# import json
# import csv
# with open('data.json', 'r') as json_file:
#     data_dict = json.load(json_file)
# csv_filename = 'data.csv'
# with open(csv_filename, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=';')
#     csv_writer.writerow(['person_id', 'name', 'age'])
#     for person_id, (name, age) in data_dict.items():
#         csv_writer.writerow(['person ' + str(person_id), name, age])
'''
Задачи на исключения

6.	Опишите конструкцию отлова ошибок, так чтобы выводило, какую ошибку вы сделали. Код представлен ниже:
x = (1, 2, 5, 7)
x = x  / 2
print(x)
'''

# try:
#     x = (1, 2, 5, 7)
#     x = x / 2
#     print(x)
# except Exception as e:
#     print(type(e))


'''
7.	Напишите программу которые будет ловить IndexError, когда вы пытаетесь взять индекс элемента, которого нет в списке.
'''
# try:
#     x = (1, 2, 5, 7)
#     print(x[4])
# except  IndexError:
#     print("IndexError")

'''
8.	Напишите программу которые будет ловить TypeError, когда вы пытаетесь скаткатенировать строку и число.
'''
# try:
#     x = 1 + "1"
#     print(x)
# except  TypeError:
#     print("TypeError")


'''
9.	Напишите программу которые будет ловить FileNotFoundError, когда вы пытаетесь открыть файл для чтения,
которого не существует.
'''
# try:
#     with open(qwe.txt):
# except FileNotFoundError:
#     print(FileNotFoundError)


'''
10.	Дан список. Пользователь не знает его размер. Программа должна бросить исключение TypeError,
когда пользователь пытается удалить элемент которого нет в списке.
'''
# def remove_element_from_list(my_list, element):
#     try:
#         my_list.remove(element)
#         print(f"Элемент {element} удален из списка.")
#     except ValueError:
#         raise TypeError(f"Элемент {element} отсутствует в списке. Невозможно удалить.")
#
# # Пример использования
# my_list = [1, 2, 3, 4, 5]
#
# try:
#     element_to_remove = int(input("Введите элемент для удаления: "))
#     remove_element_from_list(my_list, element_to_remove)
# except TypeError as e:
#     print(f"Ошибка: {e}")
# except ValueError:
#     print("Ошибка: Введенное значение не является числом.")


'''
Дополнительные задачи *

11.	Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое
частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
вывести лексикографически первое. Для решение вам необходимо открыть файл для чтения 7.txt .
Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3

12.	Вашей задачей будет восстановление исходной строки обратно. Напишите программу, которая считывает из файла строку,
соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Для решение вам необходимо открыть файл для чтения 8.txt .

Sample Input:
a3b4c2e10b1
Sample Output:
Aaabbbbcceeeeeeeeeeb
'''
