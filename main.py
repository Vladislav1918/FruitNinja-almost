import pygame  # Импортируем pygame, чтобы его можно было использовать
import random  # Импортируем рандом чтобы в дальнейшем его использовать для более интересного игрового процесса
import math    # Модуль для работы с математикой
import time

pygame.init()  # Инициализируем pygame

# Настройки экрана
screen_width, screen_height = 1900, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FruitNinja")  # Создаем заголовок

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)

# Загрузка изображений
Home_screen = pygame.image.load("Paiting/Home_screen_1900_na_1000.png")
Game_screen = pygame.image.load("Paiting/screen_of_game(1900_na_1000).png")
ves_arbuz = pygame.image.load("Fruits/целый_арбуз.png").convert_alpha()#метод который оптимизиркет изображение и сохраняеть альфа-какнал(прозрачность)
left_part_of_arbuz = pygame.image.load("Fruits/левая_половинка.png")
right_part_of_arbuz = pygame.image.load("Fruits/правая_половинка_арбуза.png")

ves_arbuz_rect = ves_arbuz.get_rect()#Создаем прямоугольник для картинки арбуза( по умолочанию сохраняется на координатах 0, 0)
current_arbuz_rect = ves_arbuz_rect#Сохраняем ves_arbuz_rect в current_arbuz_rect, для того, чтобы отслеживать перемещение арбуза


# Начальные параметры арбуза
x0 = 0  # Начальная позиция x
y0 = screen_height - 50  # Начальная позиция y (например, 950)
Vx = 0  # Горизонтальная скорость
Vy = 0  # Вертикальная скорость
time_elapsed = 0#Время прошедшее с момет=нта запуска полета
shag_time = 0.02# Уменьшили шаг времени для плавной анимации
g = 1000  # Увеличили значение гравитации для заметного эффекта (подберите подходящее значение)
fruit_active = False  # Инициализируем как False, чтобы арбуз инициализировался при запуске
rotation_angle = 0#Команда которая сохраняет текущий угол вращения
rotation_speed = 5#Команда которая сохраняет скорость вращения обьекта
napravlenie = 300#Переменная отвечает за направление обьекта
shag_napravleniya = 10#Переменная которая узнает шаг направление т.е на сколько он будет изменяться за кадр
ugol_poleta = random.uniform(math.radians(70), math.radians(110))
proverka_nacgatiy = 0
clock = pygame.time.Clock()  # обьект который контролирует FPS и измеряет количество времени между кадрами
koordination_for_arbuz  = None


slice_falling = False
slices_active = False
left_part_fall_pos = []# список для координат левой дольки арбуза
right_part_fall_pos = []# список для координат правой дольки арбуза
slises_rotation_angle = 0# текущий угол наклона долек арбуза
slises_angle_change = 0# Переменная изменения угла для долек арбуза
slices_fall_speed_y = -10
rotated_left_part_of_arbuz = None
rotated_right_part_of_arbuz = None
napravlenie_slises = 300
rotated_left_part_of_arbuz_rect = None
rotated_right_part_of_arbuz_rect = None


# Основной цикл
running = True  # Переменная для основного цикла
proverka_ekranov = 0

# Создаем шрифт для кнопок
font = pygame.font.SysFont(None, 50)

# Создаем кнопки
text_start = font.render("Начать игру", True, red)
text_rect_start = text_start.get_rect(center=(screen_width // 2, 210))

text_join = font.render("Присоединиться к игре", True, red)
text_rect_join = text_join.get_rect(center=(screen_width // 2, 255))

text_settings = font.render("Настройки", True, red)
text_rect_settings = text_settings.get_rect(center=(screen_width // 2, 310))

text_exit = font.render("Выход", True, red)
text_rect_exit = text_exit.get_rect(center=(screen_width // 2, 350))

button_rect = pygame.Rect(300,200,200,100)



def start_screen():
    screen.blit(Home_screen, (0, 0))
    screen.blit(text_start, text_rect_start)
    screen.blit(text_join, text_rect_join)
    screen.blit(text_settings, text_rect_settings)
    screen.blit(text_exit, text_rect_exit)
# 1  - падение долек 2 - генерация новго арбуза 3- движение арбуза



def gameplay():
    global fruit_active, y0, Vx, Vy, time_elapsed, x0, g, shag_time, napravlenie, ugol_poleta, current_arbuz_rect,slices_active, slises_rotation_angle, rotated_left_part_of_arbuz,  rotated_right_part_of_arbuz, rotated_left_part_of_arbuz_rect, rotated_right_part_of_arbuz_rect
    screen.blit(Game_screen, (0, 0))

    if proverka_nacgatiy == 1 and koordination_for_arbuz:#Дольки отображаются если koordination_for_arbuz заполнена т.е хранить координаты
        rotated_left_part_of_arbuz = pygame.transform.rotate(left_part_of_arbuz, napravlenie_slises)
        rotated_right_part_of_arbuz = pygame.transform.rotate(right_part_of_arbuz, napravlenie_slises)

        rotated_left_part_of_arbuz_rect = rotated_left_part_of_arbuz.get_rect(center=(left_part_of_arbuz_x, left_part_of_arbuz_y))
        rotated_right_part_of_arbuz_rect = rotated_right_part_of_arbuz.get_rect(center=(right_part_of_arbuz_x, right_part_of_arbuz_y))

        vrashenie_dolek()







    if slices_active == False and fruit_active == False:#2
        x0 = random.randint(400, screen_width - 400)  # randit работает только с целыми числами
        V0 = random.uniform(1300, 1200)  # Скорость подобрана экспериментально
        ugol_poleta = random.uniform(math.radians(70), math.radians(110))#Выдаем рандомное значение угла полета
        Vx = V0 * math.cos(ugol_poleta)#Делаем подсчет
        Vy = V0 * math.sin(ugol_poleta)#Делаем подсчет
        time_elapsed = 0# Переменная, которая считает сколько времени прошло с начала движения арбуза
        fruit_active = True# И переменая fruit_active должна равняться True, чтобы игра заиграла

    # Расчет текущей позиции арбуза
    x = x0 + Vx * time_elapsed
    y = y0 - (Vy * time_elapsed - 0.5 * g * time_elapsed ** 2)


    napravlenie += 3
    if ugol_poleta <= 90:
        rotated_image = pygame.transform.rotate(ves_arbuz, (napravlenie - (2  * napravlenie)))#команда отвечает за то, чтобы арбуз мог крутитсья вправо
    else:
        rotated_image = pygame.transform.rotate(ves_arbuz, napravlenie)
    rotated_image_rect =  rotated_image.get_rect(center=(int(x), int(y)))#center
    screen.blit(rotated_image, rotated_image_rect.topleft)#параметр topleft передает координаты левого верхнего угла rotated_image

    time_elapsed += shag_time
    current_arbuz_rect = rotated_image_rect

    # Проверка выхода за нижнюю границу экрана
    if y >= screen_height or x < -ves_arbuz.get_width() or x > screen_width:
        fruit_active = False


def vrashenie_dolek():
    global slices_fall_speed_y, left_part_of_arbuz_y, left_part_of_arbuz_x, right_part_of_arbuz_x, right_part_of_arbuz_y, rotated_left_part_of_arbuz, rotated_right_part_of_arbuz, napravlenie_slises, rotated_right_part_of_arbuz_rect, rotated_left_part_of_arbuz_rect, napravlenie_slises

    left_part_of_arbuz_y -= slices_fall_speed_y
    right_part_of_arbuz_y -= slices_fall_speed_y

    screen.blit(rotated_left_part_of_arbuz, rotated_left_part_of_arbuz_rect)
    screen.blit(rotated_right_part_of_arbuz, rotated_right_part_of_arbuz_rect)
    napravlenie_slises += 10
    if left_part_of_arbuz_y <= 0:
        print("Дольки упали")






# Основной цикл игры
while running:#Некое тело, т.е отвечает за действие
    #Начало цикла событий
    for event in pygame.event.get():#ОТвечает за события т.е некий мозг программы
        print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            print(mouse_pos)

            if text_rect_start.collidepoint(mouse_pos):
                proverka_ekranov = 1

            elif text_rect_join.collidepoint(mouse_pos):
                print("Вы присоединились к игре")

            elif text_rect_settings.collidepoint(mouse_pos):  # Убедитесь, что отступ правильный
                print("Вы открыли настройки")

            elif text_rect_exit.collidepoint(mouse_pos):
                print("Вы вышли")
                running = False  # Выход из игры при нажатии на "Выход"

            if current_arbuz_rect.collidepoint(mouse_pos):  # Проверяем, было ли нажатие на арбуз
                koordination_for_arbuz = event.pos
                slises_rotation_angle = 0  # ОБНУЛЯЕМ УГОЛ НАКЛОНА
                slices_active = True  # Даем значение True, т.к мы попали по арбузу
                left_part_fall_pos = koordination_for_arbuz
                right_part_fall_pos = koordination_for_arbuz[0] + 200, koordination_for_arbuz[-1]
                left_part_of_arbuz_x = left_part_fall_pos[0]
                left_part_of_arbuz_y = left_part_fall_pos[-1]
                right_part_of_arbuz_x = right_part_fall_pos[0]
                right_part_of_arbuz_y = right_part_fall_pos[-1]
                proverka_nacgatiy = 1


    #Конец цикла событий
    #Начало цикла While(начало действия)

    if proverka_ekranov == 1:
        dt = clock.tick(60) / 1000.0#время между кадрами за секунду(установили FPS = 60)
        gameplay()

    else:
        start_screen()

    pygame.display.flip()#Обновление экрана
    #Конец цикла действия

pygame.quit()