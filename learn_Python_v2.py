# ⚡ Мини-практика (важно)
# Напиши код, который:
# Создаёт список из 3 чисел
# Добавляет туда ещё одно число
# Создаёт словарь с ключами:
# name
# age
# Пишет функцию, которая принимает имя и выводит:
# Привет, <имя>
# Напиши код прямо сюда.
# Не переживай если будут ошибки — я их разберу.
from fontTools.misc.cython import returns
from telethon.tl.types import User

# def list_cr():
#     list = int(1)
#     if list > 0:
#         list += 1
#     return list
#
# print(list_cr())
#
#
# users = [
#     {"name": "Алексей", "age": 25},
#     {"name": "Мария", "age": 30}
# ]
#
# def users_name(users):
#     for user in users:
#         if user['age'] >= 26:
#             print(f"{user['name']} - {user['age']}")
#
# users_name(users)
#
# users = [
#     {"name": "Алексей", "age": 25},
#     {"name": "Мария", "age": 30}
# ]
#
# def print_users_older_than(users, age_limit):
#     for user in users:
#         if user['age'] > age_limit:
#             print(f"{user['name']} - {user['age']} лет")
#
#
#
#
# def get_users_older_than(users, age_limit):
#     new_list = []
#     for user in users:
#         if user['age'] > age_limit:
#             new_list.append(user)
#     return new_list
#
# result = get_users_older_than(users, 26)
# print(result)
#
# users = [
#     {"name": "Алексей", "age": 25},
#     {"name": "Мария", "age": 30}
# ]
#
# def get_average_age(users):
#     sum_age = 0
#     for user in users:
#         sum_age = user['age'] + sum_age
#     sum_age = sum_age / len(users)
#     return sum_age
#
# result = get_average_age(users)
# print(result)
#
# def get_oldest_user(users):
#     if not users:
#         return None
#
#     oldest_user = users[0]
#
#     for user in users:
#         if user['age'] > oldest_user['age']:
#             oldest_user = user
#     return oldest_user
#
# result = get_oldest_user(users)
# print(result)
#
# users = [
#     {"name": "Алексей", "age": 25},
#     {"name": "Мария", "age": 30}
# ]
#
# def add_user(users,name,age):
#     new_user = {
#         "name": name,
#         "age": age
#     }
#
#     users.append(new_user)
#     return users
#
# user_nm = input("Введи свое имя: ")
# user_ag = int(input("Введи свой возраст(полных лет): "))
# add_user(users,user_nm,user_ag)
# print(users)

# users = [
#     {"name": "Алексей", "age": 25},
#     {"name": "Мария", "age": 30}
# ]
#
# def update_users_age(users,name,new_age):
#     for user in users:
#         if user["name"] == name:
#             user["age"] = new_age
#     return users
#
# result = update_users_age(users, "Алексей", "30")
# print(result)
#


# numbers = [1,2,3,4,5]
#
# def sv_tw(num):
#     for n in numbers:
#         result = n * 2
#         print(result)
#     return result

# word_user = "олдос Хаксли родился в 1894 году."
# print(f"{word_user[0].upper() + word_user[1:]}")

# Решение задания 4 Главы 6 ПРАКТИМУМ.
# egv = []
#
# word = "Где это? Кто это? Когда это?"
# result = word.split("?")
# for item in result:
#     if item != "":
#         egv += (item.strip() + "?")
#
# print(egv)


# print(f"{result}")


# Задача 5 Глава 6 Практикум
# Преврати список "Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."
# в грамматически правильное предложение.
# Каждое слово должно отделяться пробелом, но между словом «забор» и следующей за ним точкой пробела быть не должно. (Не забывайте, вы выучили
# метод, превращающий список строк в единую строку.)

# user_list = ["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."]
# one = " ".join(user_list[:-1])
# second = "."
# result = one + second
# print(result)

# v2 от гпт

# user_list = ["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."]
# one = " ".join(user_list[:-1]) + "."
# print(one)

# Замените каждое вхождение буквы "о" в строке "Ребенок - зеркало поступков родителей." цифрой 0
# word = "Ребенок - зеркалО поступков рОдителей."
# one_revers = word.replace("о", "0").replace("О", "0")
# print(one_revers)


#Используйте метод, чтобы определить индекс символа "м" в строке "Хэмингуэй".
# author = "Хэмингуэй"
# print(author.find("м"))

# Найдите в своей любимой книге диалог (с кавычками) и превратите его в
# строку.
# "Если любишь цветок — хорошо просто смотреть на него, — сказал Маленький принц. — Тогда он существует для тебя среди всех звёзд."

# text = '"Если любишь цветок — хорошо просто смотреть на него, — сказал Маленький принц. — Тогда он существует для тебя среди всех звёзд."'
# print(text)

# Создайте строку «тритритри», используя конкатенацию , а затем сделайте то
# же самое, только с помощью умножения
#
# a = "три"
# result = a + a + a
# print(result)
# a = "три"
# result = a * 3
# print(result)

#
# user_list1 = [8, 19, 148, 4]
# user_list2 = [9, 1, 33, 83]
# user_list3 = []
#
# for i in user_list1:
#     for j in user_list2:
#         user_list3.append(i * j)
# print(user_list3)

# numbers = [5, 12, 7, 20, 3]
# new_numbers = [i for i in numbers if i > 10]
# print(new_numbers)

# fruits = ['apple', 'banana', 'kiwi', 'mango']
# new_fruits = []
# for i, fruit in enumerate(fruits):
#     if i % 2 == 0:
#         new_fruits.append(fruit)
# print(new_fruits)

# list1 = [2, 4, 6]
# list2 = [3, 5, 7]
# new_list = []
#
# for i in list1:
#     for j in list2:
#         result = i * j
#         if result > 20:
#             new_list.append(result)
# print(new_list)
#
# import os
# import csv
# user_list = [
#     ["Звездные войны", "Терминатор", "Искусственный интеллект"],
#     ["Дурак", "Матильда", "Левиафан"],
#     ["Люди в черном", "Я - робот", "Эволюция"]
# ]
# path = os.path.expanduser("~/PycharmProjects/PythonProject1/st.csv")
# with open(path, "w", newline="", encoding="utf-8") as f:
#     w = csv.writer(f)
#     for i in user_list:
#         w.writerow(i)
#
# with open(path, "r", encoding="utf-8") as f:
#     reader = csv.reader(f, delimiter=",")
#     for row in reader:
#         print(", ".join(row))
#
#
#
#
# import os
# import csv
#
# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# path = os.path.expanduser("~/PycharmProjects/PythonProject1/numbers.csv")
# with open(path, "w", newline="", encoding="utf-8") as csvfile:
#     w = csv.writer(csvfile)
#     w.writerows(numbers)
# with open(path, "r", newline="", encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(f"{', '.join(row)} → сумма: {sum(map(int, row))}")
#

#
# class Cat:
#     def meow(self):
#         print("MeOw")
#
# cat1 = Cat()
# cat2 = Cat()
#
# cat1.name = "Мурзик"
# cat2.name = "Барсик"
# cat1.age = 3
# cat2.age = 2
# cat1.meow()
#
# print(cat1.name)
# print(cat1.age)
# print(cat2.name)
# print(cat2.age)

# class Cat:
#     def meow(self):
#         print("Мяу! Ёпта")
#
# cat1 = Cat()
# cat1.meow()
#
#


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Привет, меня зовут {self.name} и мне {self.age} лет")
#
# person = Person("Алекс", 37)
# person.introduce()

#
# class Player:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def show_info(self):
#         if self.hp <= 0:
#             print(f"Игрок {self.name} имеет {self.hp} HP примини ressorection heal!")
#         else:
#             print(f"Игрок {self.name} имеет {self.hp} HP")
#
#     def take_damage(self, damage):
#         self.hp -= damage
#         if self.hp <= 0:
#             print(f"Игрок {self.name} получает критический урон {damage} HP, его здоровье {self.hp} HP теперь необходимо приминить лечение для продолжения игры.")
#         elif self.hp <= 30:
#             print(f"Игрок {self.name} получает урон {damage} HP, его здоровье {self.hp} HP необходимо приминить лечение!")
#         else:
#             print(f"Игрок {self.name} получает урон {damage} HP и теперь имеет {self.hp} HP")
#
#     def heal(self, amount):
#         self.hp += amount
#         if self.hp <= 0:
#             print(f"Игрок {self.name} неспособен продолжать")
#             return
#         elif self.hp <= 30:
#             print(f"Игрок {self.name} приминяет greater heal {amount} HP и получает {self.hp * 3} полное восстановление HP.")
#         else:
#             print(f"Игрок {self.name} применяет пополняет свое здоровье на {amount} HP и теперь имеет {self.hp} HP")
#
#
# player1 = Player("Norwway", 100)
# player1.show_info()
# player1.heal(10)
# player1.take_damage(110)
# player1.show_info()
# player1.heal(25)
# player1.show_info()


from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'
app.run(port=8000)
