'''
1.	Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения этих переменных.
Добавить функцию, которая находит сумму значений этих переменных,
и функцию которая находит наибольшее значение из этих двух переменных.
'''
#
# class TwoVariables:
#     def __init__(self, var1, var2):
#         self.var1 = var1
#         self.var2 = var2
#
#     def display_variables(self):
#         print(f"Variable 1: {self.var1}")
#         print(f"Variable 2: {self.var2}")
#
#     def modify_variables(self, new_var1, new_var2):
#         self.var1 = new_var1
#         self.var2 = new_var2
#         print("Variables modified.")
#
#     def sum_variables(self):
#         return self.var1 + self.var2
#
#     def max_variable(self):
#         return max(self.var1, self.var2)
#
# my_variables = TwoVariables(5, 8)
#
# my_variables.display_variables()
# my_variables.modify_variables(10, 15)
# my_variables.display_variables()
#
# sum_result = my_variables.sum_variables()
# print(f"Sum of variables: {sum_result}")
#
# max_result = my_variables.max_variable()
# print(f"Max variable value: {max_result}")

'''
2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу
в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.
Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяющее получить его текущее состояние.
Написать программу, демонстрирующую все возможности класса.
'''
# class DecimalCounter:
#     def __init__(self, min_value=0, max_value=10, initial_value=None):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.value = initial_value if initial_value is not None else min_value
#
#     def increment(self):
#         if self.value < self.max_value:
#             self.value += 1
#         else:
#             print("Превышено максимальное значение. Счетчик не увеличен.")
#
#     def decrement(self):
#         if self.value > self.min_value:
#             self.value -= 1
#         else:
#             print("Превышено минимальное значение. Счетчик не уменьшен.")
#
#     @property
#     def current_value(self):
#         return self.value
#
# # Пример использования
# counter1 = DecimalCounter()  # Инициализация счетчика с значениями по умолчанию
# print(f"Текущее значение счетчика 1: {counter1.current_value}")
#
# counter2 = DecimalCounter(min_value=-5, max_value=5, initial_value=3)  # Инициализация с произвольными значениями
# print(f"Текущее значение счетчика 2: {counter2.current_value}")
#
# # Увеличиваем значение счетчика 1
# counter1.increment()
# print(f"Новое значение счетчика 1: {counter1.current_value}")
#
# # Уменьшаем значение счетчика 2
# counter2.decrement()
# print(f"Новое значение счетчика 2: {counter2.current_value}")
#
# # Превышаем максимальное значение
# for _ in range(15):
#     counter2.increment()
#
# # Проверяем текущее значение после превышения максимального значения
# print(f"Текущее значение счетчика 2 после превышения: {counter2.current_value}")


'''
3.	Реализуйте класс Shop. Предусмотреть возможность работы с произвольным числом продуктов,
поиска продуктов по названию, добавления их в магазин и удаления продуктов из него.
4.	Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка имеет ограниченную вместимость,
которая выражается целым числом – количеством монет(capacity -вместимость), которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в
копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид:

class MoneyBox:
    def__init__(self, capacity) :
    #конструктор с аргументом- вместимость копилки
    def can_add(self,v)
    #True, если можно добавить v монет, False иначе
    def add(self,v)
    #положить v монет в копилку

При создании копилки, число монет в ней равно 0.
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.
'''

# class MoneyBox:
#     def __init__(self, capacity):
#         # Конструктор с аргументом - вместимость копилки
#         self.capacity = capacity
#         self.coins_inside = 0
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         return self.coins_inside + v <= self.capacity
#
#     def add(self, v):
#         # Положить v монет в копилку
#         if self.can_add(v):
#             self.coins_inside += v
#             print(f"Добавлено {v} монет. Текущее количество монет в копилке: {self.coins_inside}")
#         else:
#             print("Превышена вместимость копилки. Невозможно добавить монеты.")
#
# # Пример использования
# money_box = MoneyBox(10)  # Создаем копилку с вместимостью 10 монет
#
# # Полагаем 5 монет (вместимость копилки становится 5)
# money_box.add(5)
#
# # Попытка добавить еще 7 монет (превышение вместимости)
# money_box.add(7)
#
# # Полагаем еще 3 монеты (вместимость становится 8)
# money_box.add(3)