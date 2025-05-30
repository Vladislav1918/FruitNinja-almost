import math
import random
import pygame
class Fruits:#создаем класс
    def __init__(self,x,y,image, screen_width, screen_height):#КОНСТРУКТОР класса - указываеи обязательные параметры при создантт обьекта      self - общее название для всех обьеков класса
        # Уникальные параметры - у каждого обьекта они разные
        self.x = x#сохраняем параматры x в перменную self.x
        self.y = y#начальная позиция для y
        self.image = image#сохраняем изображение для фрукта


        # общие параметры -
        self.screen_width = 1900
        self.screen_height = 1000
        self.active = False#сохраняем активность обьекта
        self.Vx = 0#сохраняем горизонтальную  скорость обьекта
        self.Vy = 0#сохраняем вертекальную  скорость обьекта
        #self.rect = image.get_rect()
        self.time_elapsed = 0#сохраняем время с начала полета обьекта
        self.g = 1000  # Гравитация
        self.rotation_speed = 5  # Скорость вращения
        self.fruit_types = [
            {
                "name": "watermelon",
                "whole": pygame.image.load("Fruits/целый_арбуз.png").convert_alpha(),  # Здесь будет изображение целого арбуза
                "left_half": pygame.image.load("Fruits/левая_половинка.png").convert_alpha(),  # Здесь будет изображение левой половинки
                "right_half": pygame.image.load("Fruits/правая_половинка_арбуза.png").convert_alpha(),  # Здесь будет изображение правой половинки
                "points": 1
            },
            {
                "name": "apple",
                "whole": pygame.image.load("Fruits/apple(1).png"),
                "left_half": pygame.image.load("Fruits/left_part_of_apple.png"),
                "right_half": pygame.image.load("Fruits/right_part_of_apple.png"),
                "points": 1
            }
        ]



    def launch(self):# Создали МЕТОД для класса fruits
        self.active = True
        angle = random.uniform(math.radians(70), math.radians(110))  # сохраняем угол палета обьекта
        speed = random.uniform(1000, 1200)
        self.Vx = speed * math.cos(angle)# Рассчитываем скорость полета
        self.Vy = speed * math.sin(angle)# Рассчитываем скорость полета
    def create_fruits(self):
        random_fruits = random.choice(self.fruit_types)# метод random.choice позволяет взять рандомный параметр из списка
        self.active = True
        self.x = random.randint(400, self.screen_width - 400)
        self.y = 1000
        angle = random.uniform(math.radians(70), math.radians(110))  # сохраняем угол палета обьекта
        speed = random.uniform(1000, 1200)
        self.Vx = speed * math.cos(angle)  # Рассчитываем скорость полета
        self.Vy = speed * math.sin(angle)  # Рассчитываем скорость полета



















arbuz = Fruits(x=0,y=0,image=1)# создал обьект класса
print(arbuz.image)# выводим значение image у обьекта arbuz

