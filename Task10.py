'''

1.	Создайте систему управления задачами с использованием классов. Реализуйте классы "Task", "Project" и
"ProjectManager". Каждая задача должна содержать описание, статус (выполнена или нет) и срок выполнения.
Проект должен включать в себя список задач и методы для добавления новой задачи, отметки задачи как выполненной и
вывода списка всех задач.
'''
#
# from datetime import datetime, timedelta
#
# class Task:
#     def __init__(self, description, deadline):
#         self.description = description
#         self.status = "Not Done"
#         self.deadline = deadline
#
#     def mark_as_done(self):
#         self.status = "Done"
#
#     def __str__(self):
#         return f"Task: {self.description}, Status: {self.status}, Deadline: {self.deadline}"
#
# class Project:
#     def __init__(self, name):
#         self.name = name
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def mark_task_as_done(self, task_index):
#         if 0 <= task_index < len(self.tasks):
#             self.tasks[task_index].mark_as_done()
#             print(f"Task '{self.tasks[task_index].description}' marked as done.")
#         else:
#             print("Invalid task index.")
#
#     def display_tasks(self):
#         print(f"Tasks in project '{self.name}':")
#         for task in self.tasks:
#             print(task)
#
# class ProjectManager:
#     def __init__(self):
#         self.projects = []
#
#     def create_project(self, name):
#         project = Project(name)
#         self.projects.append(project)
#         print(f"Project '{name}' created.")
#
#     def add_task_to_project(self, project_index, task):
#         if 0 <= project_index < len(self.projects):
#             self.projects[project_index].add_task(task)
#             print(f"Task '{task.description}' added to project '{self.projects[project_index].name}'.")
#         else:
#             print("Invalid project index.")
#
#     def mark_task_as_done_in_project(self, project_index, task_index):
#         if 0 <= project_index < len(self.projects):
#             self.projects[project_index].mark_task_as_done(task_index)
#         else:
#             print("Invalid project index.")
#
#     def display_projects(self):
#         print("Projects:")
#         for i, project in enumerate(self.projects):
#             print(f"{i}. {project.name}")
#
# # Пример использования
# task1 = Task("Complete assignment", datetime.now() + timedelta(days=5))
# task2 = Task("Review project proposal", datetime.now() + timedelta(days=3))
#
# manager = ProjectManager()
#
# manager.create_project("Work")
# manager.create_project("Personal")
#
# manager.add_task_to_project(0, task1)
# manager.add_task_to_project(1, task2)
#
# manager.display_projects()
# manager.projects[0].display_tasks()
#
# manager.mark_task_as_done_in_project(0, 0)
#
# manager.projects[0].display_tasks()

'''
2.	Создайте систему для управления бронированием билетов в авиакомпании. Реализуйте классы "Passenger",
"Ticket", "Flight" и "Airline ". Каждый пассажир должен иметь атрибуты, такие как имя и фамилия.
Билет должен содержать информацию о пассажире и маршруте полета. Рейс должен включать в себя список зарезервированных
билетов. Авиакомпания должна иметь методы для бронирования билета, отмены брони и отображения списка зарезервированных
билетов.
'''
from datetime import datetime, timedelta

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.status = "Not Done"
        self.deadline = deadline

    def mark_as_done(self):
        self.status = "Done"

    def __str__(self):
        return f"Task: {self.description}, Status: {self.status}, Deadline: {self.deadline}"

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()
            print(f"Task '{self.tasks[task_index].description}' marked as done.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print(f"Tasks in project '{self.name}':")
        for task in self.tasks:
            print(task)

class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)
        print(f"Project '{name}' created.")

    def add_task_to_project(self, project_index, task):
        if 0 <= project_index < len(self.projects):
            self.projects[project_index].add_task(task)
            print(f"Task '{task.description}' added to project '{self.projects[project_index].name}'.")
        else:
            print("Invalid project index.")

    def mark_task_as_done_in_project(self, project_index, task_index):
        if 0 <= project_index < len(self.projects):
            self.projects[project_index].mark_task_as_done(task_index)
        else:
            print("Invalid project index.")

    def display_projects(self):
        print("Projects:")
        for i, project in enumerate(self.projects):
            print(f"{i}. {project.name}")

# Пример использования
task1 = Task("Complete assignment", datetime.now() + timedelta(days=5))
task2 = Task("Review project proposal", datetime.now() + timedelta(days=3))

manager = ProjectManager()

manager.create_project("Work")
manager.create_project("Personal")

manager.add_task_to_project(0, task1)
manager.add_task_to_project(1, task2)

manager.display_projects()
manager.projects[0].display_tasks()

manager.mark_task_as_done_in_project(0, 0)

manager.projects[0].display_tasks()

'''
3.	Создать абстрактный класс «Alive». Определить наследуемые классы – «Fox», «Rabbit» и «Plant».
Лисы едят кроликов. Кролики едят растения. Растение поглощают солнечный свет. Представители каждого класса могут
умереть, если достигнут определенного возраста или для них не будет еды. Напишите виртуальные методы поедания и
определения состояния живых существа (живые или нет, в зависимости от достижения предельного возраста и наличия еды
(входной параметр)).
'''

# from abc import ABC, abstractmethod
# import random
#
# class Alive(ABC):
#     def __init__(self, age_limit):
#         self.age = 0
#         self.age_limit = age_limit
#         self.alive = True
#
#     @abstractmethod
#     def eat(self, food_available):
#         pass
#
#     def is_alive(self):
#         return self.alive and self.age < self.age_limit
#
# class Fox(Alive):
#     def __init__(self):
#         super().__init__(age_limit=5)
#
#     def eat(self, food_available):
#         if food_available:
#             print("Fox is eating a rabbit.")
#         else:
#             print("Fox has no food.")
#             self.alive = False
#
# class Rabbit(Alive):
#     def __init__(self):
#         super().__init__(age_limit=3)
#
#     def eat(self, food_available):
#         if food_available:
#             print("Rabbit is eating a plant.")
#         else:
#             print("Rabbit has no food.")
#             self.alive = False
#
# class Plant(Alive):
#     def __init__(self):
#         super().__init__(age_limit=10)
#
#     def eat(self, food_available):
#         if food_available:
#             print("Plant is absorbing sunlight.")
#         else:
#             print("Plant has no sunlight.")
#             self.alive = False
#
# # Пример использования
# fox = Fox()
# rabbit = Rabbit()
# plant = Plant()
#
# for _ in range(6):
#     fox.eat(random.choice([True, False]))
#     fox.age += 1
#     print(f"Fox is alive: {fox.is_alive()}")
#
# for _ in range(4):
#     rabbit.eat(random.choice([True, False]))
#     rabbit.age += 1
#     print(f"Rabbit is alive: {rabbit.is_alive()}")
#
# for _ in range(11):
#     plant.eat(random.choice([True, False]))
#     plant.age += 1
#     print(f"Plant is alive: {plant.is_alive()}")
