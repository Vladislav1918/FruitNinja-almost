import pygame  # Импортируем pygame, чтобы его можно было использовать
import random  # Импортируем рандом чтобы в дальнейшем его использовать для более интересного игрового процесса
import math    # Модуль для работы с математикой
import time

pygame.init()  # Инициализируем pygame
pygame.mixer.init()# Добавляем микшер в нашу программу

# Настройки экрана
screen_width, screen_height = 1900, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FruitNinja")  # Создаем заголовок

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)

# Загрузка изображений
#метод  convert_alpha() оптимизиркет изображение и сохраняеть альфа-какнал(прозрачность), делает незанетые пиксекли прозрачными
Home_screen = pygame.image.load("Paiting/Home_screen_1900_na_1000.png").convert_alpha()
Game_screen = pygame.image.load("Paiting/screen_of_game(1900_na_1000).png").convert_alpha()
ves_arbuz = pygame.image.load("Fruits/целый_арбуз.png").convert_alpha()
left_part_of_arbuz = pygame.image.load("Fruits/левая_половинка.png").convert_alpha()
right_part_of_arbuz = pygame.image.load("Fruits/правая_половинка_арбуза.png").convert_alpha()
bomba = pygame.image.load("Fruits/bomb.png").convert_alpha()




# Музыка и музыкальные эффекты
music_cutting = pygame.mixer.Sound("Music_effects/sound_for_kill_arbuz.wav")
music_brosok_fruit = pygame.mixer.Sound("Music_effects/brosok_fruit.wav")
music_vzrif_arbuza = pygame.mixer.Sound("Music_effects/vzrif_bombi.wav")





# Переменные для бомбы
x0_bomba = 0 # Начальная позиция x
y0_bomba = screen_height - 50# Начальная позиция y (например, 950)
Vy_bomba = 0 # Вертикальная скорость
Vx_bomba = 0# Горизонтальная скорость
bomba_active = False
koordination_for_bomba = None
bomba_rect = bomba.get_rect()
current_bomba_rect = bomba_rect
bomba_active = False


# Перменные для арбуза
koordination_for_vzrif  = None
fruit_active = False  # Инициализируем как False, чтобы арбуз инициализировался при запуске
ves_arbuz_rect = ves_arbuz.get_rect()#Создаем прямоугольник для картинки арбуза( по умолочанию сохраняется на координатах 0, 0)
current_arbuz_rect = ves_arbuz_rect#Сохраняем ves_arbuz_rect в current_arbuz_rect, для того, чтобы отслеживать перемещение арбуза

# Переменные для функций
x0 = 0  # Начальная позиция x
y0 = screen_height - 50  # Начальная позиция y (например, 950)
lifes = 3
bliznec_kolichestvu_nashatiy_po_arbuzu = None
Vx = 0  # Горизонтальная скорость
Vy = 0  # Вертикальная скорость
time_elapsed = 0#Время прошедшее с момента запуска полета
shag_time = 0.02# Уменьшили шаг времени для плавной анимации
g = 1000  # Увеличили значение гравитации для заметного эффекта (подберите подходящее значение)
rotation_angle = 0#Команда которая сохраняет текущий угол вращения
rotation_speed = 5#Команда которая сохраняет скорость вращения обьекта
napravlenie = 300#Переменная отвечает за направление обьекта
shag_napravleniya = 10#Переменная которая узнает шаг направление т.е на сколько он будет изменяться за кадр
ugol_poleta = random.uniform(math.radians(70), math.radians(110))
clock = pygame.time.Clock()  # обьект который контролирует FPS и измеряет количество времени между кадрами
podshet_ochkov = 0



# Переменные для долек арбуза
slice_falling = False
slices_active = False
left_part_fall_pos = []# список для координат левой дольки арбуза
right_part_fall_pos = []# список для координат правой дольки арбуза
left_part_of_arbuz_x = 0
left_part_of_arbuz_y = 0
right_part_of_arbuz_x = 0
right_part_of_arbuz_y = 0
slises_rotation_angle = 0# текущий угол наклона долек арбуза
slises_angle_change = 0# Переменная изменения угла для долек арбуза
slices_fall_speed_y = -15
rotated_left_part_of_arbuz = None
rotated_right_part_of_arbuz = None
napravlenie_slises = 300
rotated_left_part_of_arbuz_rect = None
rotated_right_part_of_arbuz_rect = None
random_speed_for_arbuz_x = random.randint(1, 5)


# Основной цикл
running = True  # Переменная для основного цикла
proverka_ekranov = 0

# Создаем шрифт для кнопок
font = pygame.font.SysFont(None, 50)

# Создаем кнопки
text_podshet_ochkov = font.render("Количество очков = " + str(podshet_ochkov), True, red)
text_podshet_ochkov_rect = text_podshet_ochkov.get_rect(topleft=(0,15))

text_lifes = font.render('Количество жизни = ' + str(lifes), True, red)
text_lifes_rect = text_lifes.get_rect(topleft=(1500 , 15))

text_start = font.render("Начать игру", True, red)
text_rect_start = text_start.get_rect(center=(screen_width // 2, 210))

text_join = font.render("Присоединиться к игре", True, red)
text_rect_join = text_join.get_rect(center=(screen_width // 2, 255))

text_settings = font.render("Настройки", True, red)
text_rect_settings = text_settings.get_rect(center=(screen_width // 2, 310))

text_exit = font.render("Выход", True, red)
text_rect_exit = text_exit.get_rect(center=(screen_width // 2, 350))

button_rect = pygame.Rect(300,200,200,100)
#3 марта


def start_screen():
    screen.blit(Home_screen, (0, 0))
    screen.blit(text_start, text_rect_start)
    screen.blit(text_join, text_rect_join)
    screen.blit(text_settings, text_rect_settings)
    screen.blit(text_exit, text_rect_exit)
# 1  - падение долек 2 - генерация новго арбуза 3- движение арбуза

def reset_game():
    global lifes, fruit_active, bomba_active, text_lifes, text_podshet_ochkov, koordination_for_arbuz, time_elapsed, slices_active, podshet_ochkov, proverka_ekranov
    lifes = 3
    fruit_active = False
    bomba_active = False
    text_lifes = font.render('Количество жизни = ' + str(lifes), True, red)
    text_podshet_ochkov = font.render("Количество очков = " + str(podshet_ochkov), True, red)
    koordination_for_arbuz = None
    time_elapsed = 0
    slices_active = False
    podshet_ochkov = 0
    proverka_ekranov = 0




def gameplay():
    global fruit_active, y0, Vx,Vx_bomba,Vy_bomba,Vy, time_elapsed, x0,x0_bomba, g, shag_time, napravlenie, ugol_poleta, current_arbuz_rect,slices_active, slises_rotation_angle, rotated_left_part_of_arbuz,  rotated_right_part_of_arbuz, rotated_left_part_of_arbuz_rect, rotated_right_part_of_arbuz_rect, slices_fall_speed_y, bliznec_kolichestvu_nashatiy_po_arbuzu, lifes, text_lifes, proverka_ekranov, koordination_for_arbuz, podshet_ochkov, text_podshet_ochkov, bomba, bomba_active, current_bomba_rect
    screen.blit(Game_screen, (0, 0))
    screen.blit(text_podshet_ochkov, text_podshet_ochkov_rect)
    screen.blit(text_lifes, text_lifes_rect)



    if proverka_ekranov == 1 and koordination_for_arbuz:#Дольки отображаются если koordination_for_arbuz заполнена т.е хранить координаты
        fruit_active = False

        rotated_left_part_of_arbuz = pygame.transform.rotate(left_part_of_arbuz, napravlenie_slises)
        rotated_right_part_of_arbuz = pygame.transform.rotate(right_part_of_arbuz, napravlenie_slises)

        rotated_left_part_of_arbuz_rect = rotated_left_part_of_arbuz.get_rect(center=(left_part_of_arbuz_x, left_part_of_arbuz_y))
        rotated_right_part_of_arbuz_rect = rotated_right_part_of_arbuz.get_rect(center=(right_part_of_arbuz_x, right_part_of_arbuz_y))

        vrashenie_dolek()


    if slices_active == False and fruit_active == False and bomba_active == False:

        x0 = random.randint(400, screen_width - 400)  # randit работает только с целыми числами
        V0 = random.uniform(1000, 1200)  # Скорость подобрана экспериментально
        ugol_poleta = random.uniform(math.radians(70), math.radians(110))#Выдаем рандомное значение угла полета

        x0_bomba = random.randint(400, screen_width - 400)
        V0_bomba = random.uniform(1000, 1200)# Скорость, с которой перемещается бомба

        ugol_poleta_bomba = random.uniform(math.radians(70), math.radians(110))


        Vx = V0 * math.cos(ugol_poleta)#Делаем подсчет
        Vy = V0 * math.sin(ugol_poleta)#Делаем подсчет

        Vx_bomba = V0_bomba * math.cos(ugol_poleta_bomba)
        Vy_bomba = V0_bomba * math.sin(ugol_poleta_bomba)

        time_elapsed = 0# Переменная, которая считает сколько времени прошло с начала движения арбуза
        fruit_active = True# И переменая fruit_active должна равняться True, чтобы игра заиграла
        bomba_active = True

    # Расчет текущей позиции арбуза
    x = x0 + Vx * time_elapsed
    y = y0 - (Vy * time_elapsed - 0.5 * g * time_elapsed ** 2)

    x_bomba = x0_bomba + Vx_bomba * time_elapsed
    y_bomba = y0_bomba - (Vy_bomba * time_elapsed - 0.5 * g * time_elapsed ** 2)


    napravlenie += 3
    if ugol_poleta <= 90:
        rotated_image_bomba = pygame.transform.rotate(bomba, (napravlenie - (2 * napravlenie)))
        rotated_image = pygame.transform.rotate(ves_arbuz, (napravlenie - (2  * napravlenie)))#команда отвечает за то, чтобы арбуз мог крутитсья вправо
    else:
        rotated_image_bomba = pygame.transform.rotate(bomba, (napravlenie - (2 * napravlenie)))
        rotated_image = pygame.transform.rotate(ves_arbuz, napravlenie)
    rotated_image_bomba_rect = rotated_image_bomba.get_rect(center=(int(x_bomba), int(y_bomba)))
    rotated_image_rect = rotated_image.get_rect(center=(int(x), int(y)))  # center

    if fruit_active == True:# Сделали проверку т.к без этой проверки арбуз всегда будет выводиться, а с этой строкой арбуз будет выводиться если арбуз активен
        screen.blit(rotated_image, rotated_image_rect.topleft)#параметр topleft передает координаты левого верхнего угла rotated_image
    if bomba_active == True:
        screen.blit(rotated_image_bomba, rotated_image_bomba_rect.topleft)


    time_elapsed += shag_time

    current_arbuz_rect = rotated_image_rect
    current_bomba_rect = rotated_image_bomba_rect

    # Проверка выхода за нижнюю границу экрана
    if fruit_active == True and y >= screen_height or x < -ves_arbuz.get_width() or x > screen_width:
        lifes = lifes -  1
        fruit_active = False
        music_brosok_fruit.play()# Ставим здесь вывод музыки т.к после того как упал арбуз он еще раз вылетает
        text_lifes = font.render('Количество жизни = ' + str(lifes), True, red)
        if lifes == 0:
            reset_game()
    if y >= screen_height or x < -bomba.get_width() or x > screen_width:
        bomba_active = False
        print("Бомба вылетела за экран")



def vrashenie_dolek():

    global slices_fall_speed_y, left_part_of_arbuz_y, left_part_of_arbuz_x, right_part_of_arbuz_x, right_part_of_arbuz_y, rotated_left_part_of_arbuz, rotated_right_part_of_arbuz, napravlenie_slises, rotated_right_part_of_arbuz_rect, rotated_left_part_of_arbuz_rect, napravlenie_slises, slices_active, fruit_active, proverka_nacgatiy, random_speed_for_arbuz_x, koordination_for_arbuz, proverka_ekranov

    slices_fall_speed_y += 1

    left_part_of_arbuz_x -= random_speed_for_arbuz_x
    right_part_of_arbuz_x += random_speed_for_arbuz_x
    left_part_of_arbuz_y += slices_fall_speed_y
    right_part_of_arbuz_y += slices_fall_speed_y



    screen.blit(rotated_left_part_of_arbuz, (left_part_of_arbuz_x, left_part_of_arbuz_y))
    screen.blit(rotated_right_part_of_arbuz, (right_part_of_arbuz_x, right_part_of_arbuz_y))
    napravlenie_slises -= 10


    if left_part_of_arbuz_y >= 1000 and right_part_of_arbuz_y >= 1000:

        slices_active = False

        fruit_active = False

        slices_fall_speed_y = -15

        proverka_nacgatiy = 0

        random_speed_for_arbuz_x = random.randint(1, 5)

        koordination_for_arbuz = None

        music_brosok_fruit.play()# Так же здесь т.к после того как упали дольки арбуз вылетает снова










# Основной цикл игры
while running:#Некое тело, т.е отвечает за действие
    #Начало цикла событий
    for event in pygame.event.get():#ОТвечает за события т.е некий мозг программы
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos



            if text_rect_start.collidepoint(mouse_pos) and proverka_ekranov == 0:
                music_brosok_fruit.play()# Перед вылетом арбуза выводим звук
                reset_game()
                proverka_ekranov = 1

            elif text_rect_join.collidepoint(mouse_pos):
                print("Вы присоединились к игре")

            elif text_rect_settings.collidepoint(mouse_pos):  # Убедитесь, что отступ правильный
                print("Вы открыли настройки")

            elif text_rect_exit.collidepoint(mouse_pos) and proverka_ekranov == 0:
                print("Вы вышли")
                running = False  # Выход из игры при нажатии на "Выход"

            if current_arbuz_rect.collidepoint(mouse_pos):  # Проверяем, было ли нажатие на арбуз
                music_cutting.play()
                koordination_for_arbuz = event.pos
                podshet_ochkov += 1
                text_podshet_ochkov = font.render("Количество очков = " + str(podshet_ochkov), True, red)
                screen.blit(text_podshet_ochkov, text_podshet_ochkov_rect)
                slises_rotation_angle = 0  # ОБНУЛЯЕМ УГОЛ НАКЛОНА
                slices_active = True  # Даем значение True, т.к мы попали по арбузу
                left_part_fall_pos = koordination_for_arbuz
                right_part_fall_pos = koordination_for_arbuz[0] + 200, koordination_for_arbuz[-1]
                left_part_of_arbuz_x = left_part_fall_pos[0]
                left_part_of_arbuz_y = left_part_fall_pos[-1]
                right_part_of_arbuz_x = right_part_fall_pos[0]
                right_part_of_arbuz_y = right_part_fall_pos[-1]
                proverka_ekranov = 1
                print(podshet_ochkov)

            if current_bomba_rect.collidepoint(mouse_pos):
                koordination_for_vzrif = event.pos
                bomba_active = False
                lifes -= 1
                text_lifes = font.render('Количество жизни = ' + str(lifes), True, red)
                music_brosok_fruit.play()

                if lifes == 0:
                    reset_game()

                print("Вы попали по бомбе")




    #Конец цикла событий
    #Начало цикла While(начало действия)

    if proverka_ekranov == 1:
        dt = clock.tick(60) / 1000.0#время между кадрами за секунду(установили FPS = 60)
        gameplay()

    elif proverka_ekranov == 0:
        start_screen()

    pygame.display.flip()#Обновление экрана
    #Конец цикла действия

pygame.quit()