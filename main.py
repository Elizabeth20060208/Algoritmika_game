import pygame
import pygame.mixer
pygame.init()
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) #Размер игрового окна
pygame.display.set_caption("Алгоритмика") #Название программы

#Загрузка фоновой мелодии с компьютера
pygame.mixer.music.load("sounds/bg.mp3") #Загрузка
pygame.mixer.music.play() #Запуск
pygame.mixer.music.set_volume(0.5) #Громкость

class Object(pygame.sprite.Sprite):       #Класс объектов игры
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()  #Форма: прямоугольник
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

#Точка спауна игрока
start_x = 100
start_y = 110

#Импорт изображений
bg = pygame.transform.scale(pygame.image.load("images/bg.png"), (1280, 720)) #Загрузка фона с компьютера
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (50, 55)) #Загрузка игрока с компьютера
wall = pygame.transform.scale(pygame.image.load("images/wall.png"), (120, 100)) #Загрузка стенок с компьютера(дерева)
enemy_img = pygame.transform.scale(pygame.image.load("images/enemy.png"), (60, 65)) #Загрузка врага с компьютера
mana = pygame.transform.scale(pygame.image.load("images/mana.png"), (40, 45))#Загрузка маны с компьютера

all_sprites = pygame.sprite.Group() #Создание группы всех объектов
walls = pygame.sprite.Group() #Создание группы стенок
enemies = pygame.sprite.Group() #Создание группы врагов
items = pygame.sprite.Group() #Создание группы вещей(маны)

#Создание объекта "игрок"

player = Object(player_img, start_x, start_y, 8)
all_sprites.add(player)

#Создание объектов "враги"

enemy1 = Object(enemy_img, 800, 120, 4)
all_sprites.add(enemy1)
enemies.add(enemy1)
enemy2 = Object(enemy_img, 500, 470, 4)
all_sprites.add(enemy2)
enemies.add(enemy2)
enemy3 = Object(enemy_img, 250, 300, 4)
all_sprites.add(enemy3)
enemies.add(enemy3)

#Создание объектов "вещи"(мана)

mana1 = Object(mana, 540, 300, 0)
all_sprites.add(mana1)
items.add(mana1)
mana2 = Object(mana, 40, 650, 0)
all_sprites.add(mana2)
items.add(mana2)
mana3 = Object(mana, 1150, 650, 0)
all_sprites.add(mana3)
items.add(mana3)
mana4 = Object(mana, 770, 205, 0)
all_sprites.add(mana4)
items.add(mana4)

#Стенки

wall59 = Object(wall, -90, 00, 0) #59
all_sprites.add(wall59)
walls.add(wall59)
wall1 = Object(wall, 0, 0, 0)
all_sprites.add(wall1)
walls.add(wall1)
wall2 = Object(wall, 90, 0, 0)
all_sprites.add(wall2)
walls.add(wall2)
wall3 = Object(wall, 180, 0, 0)
all_sprites.add(wall3)
walls.add(wall3)
wall4 = Object(wall, 270, 0, 0)
all_sprites.add(wall4)
walls.add(wall4)
wall5 = Object(wall, 360, 0, 0)
all_sprites.add(wall5)
walls.add(wall5)
wall6 = Object(wall, 450, 0, 0)
all_sprites.add(wall6)
walls.add(wall6)
wall7 = Object(wall, 540, 0, 0)
all_sprites.add(wall7)
walls.add(wall7)
wall8 = Object(wall, 630, 0, 0)
all_sprites.add(wall8)
walls.add(wall8)
wall9 = Object(wall, 720, 0, 0)
all_sprites.add(wall9)
walls.add(wall9)
wall10 = Object(wall, 810, 0, 0)
all_sprites.add(wall10)
walls.add(wall10)

wall11 = Object(wall, 630, 90, 0)
all_sprites.add(wall11)
walls.add(wall11)
wall12 = Object(wall, 630, 180, 0)
all_sprites.add(wall12)
walls.add(wall12)
wall13 = Object(wall, 630, 270, 0)
all_sprites.add(wall13)
walls.add(wall13)
wall14 = Object(wall, 630, 360, 0)
all_sprites.add(wall14)
walls.add(wall14)

wall15 = Object(wall, 540, 360, 0)
all_sprites.add(wall15)
walls.add(wall15)
wall16 = Object(wall, 450, 360, 0)
all_sprites.add(wall16)
walls.add(wall16)
wall17 = Object(wall, 360, 360, 0)
all_sprites.add(wall17)
walls.add(wall17)

wall18 = Object(wall, 360, 270, 0)
all_sprites.add(wall18)
walls.add(wall18)
wall19 = Object(wall, 360, 180, 0)
all_sprites.add(wall19)
walls.add(wall19)

wall20 = Object(wall, 180, 180, 0)
all_sprites.add(wall20)
walls.add(wall20)
wall21 = Object(wall, 90, 180, 0)
all_sprites.add(wall21)
walls.add(wall21)
wall58 = Object(wall, 270, 180, 0)  #58
all_sprites.add(wall58)
walls.add(wall58)

wall22 = Object(wall, 90, 270, 0)
all_sprites.add(wall22)
walls.add(wall22)
wall23 = Object(wall, 90, 360, 0)
all_sprites.add(wall23)
walls.add(wall23)

wall24 = Object(wall, 890, 0, 0)
all_sprites.add(wall24)
walls.add(wall24)
wall25 = Object(wall, 980, 0, 0)
all_sprites.add(wall25)
walls.add(wall25)
wall26 = Object(wall, 1190, 0, 0)
all_sprites.add(wall26)
walls.add(wall26)
wall27 = Object(wall, 1250, 0, 0)
all_sprites.add(wall27)
walls.add(wall27)

wall28 = Object(wall, 720, 270, 0)
all_sprites.add(wall28)
walls.add(wall28)
wall29 = Object(wall, 810, 270, 0)
all_sprites.add(wall29)
walls.add(wall29)

wall30 = Object(wall, 360, 450, 0)
all_sprites.add(wall30)
walls.add(wall30)
wall31 = Object(wall, 360, 540, 0)
all_sprites.add(wall31)
walls.add(wall31)

wall32 = Object(wall, 450, 540, 0)
all_sprites.add(wall32)
walls.add(wall32)
wall33 = Object(wall, 540, 540, 0)
all_sprites.add(wall33)
walls.add(wall33)
wall34 = Object(wall, 630, 540, 0)
all_sprites.add(wall34)
walls.add(wall34)

wall35 = Object(wall, 1250, 90, 0)
all_sprites.add(wall35)
walls.add(wall35)
wall36 = Object(wall, 1250, 180, 0)
all_sprites.add(wall36)
walls.add(wall36)
wall37 = Object(wall, 1250, 270, 0)
all_sprites.add(wall37)
walls.add(wall37)
wall38 = Object(wall, 1250, 360, 0)
all_sprites.add(wall38)
walls.add(wall38)
wall39 = Object(wall, 1250, 450, 0)
all_sprites.add(wall39)
walls.add(wall39)
wall40 = Object(wall, 1250, 540, 0)
all_sprites.add(wall40)
walls.add(wall40)
wall41 = Object(wall, 1250, 630, 0)
all_sprites.add(wall41)
walls.add(wall41)
wall42 = Object(wall, 1250, 720, 0)
all_sprites.add(wall42)
walls.add(wall42)

wall43 = Object(wall, 0, 720, 0)
all_sprites.add(wall43)
walls.add(wall43)
wall44 = Object(wall, 90, 720, 0)
all_sprites.add(wall44)
walls.add(wall44)
wall45 = Object(wall, 180, 720, 0)
all_sprites.add(wall45)
walls.add(wall45)
wall46 = Object(wall, 270, 720, 0)
all_sprites.add(wall46)
walls.add(wall46)
wall47 = Object(wall, 360, 720, 0)
all_sprites.add(wall47)
walls.add(wall47)
wall48 = Object(wall, 450, 720, 0)
all_sprites.add(wall48)
walls.add(wall48)
wall49 = Object(wall, 540, 720, 0)
all_sprites.add(wall49)
walls.add(wall49)
wall50 = Object(wall, 630, 720, 0)
all_sprites.add(wall50)
walls.add(wall50)
wall51 = Object(wall, 720, 720, 0)
all_sprites.add(wall51)
walls.add(wall51)
wall52 = Object(wall, 810, 720, 0)
all_sprites.add(wall52)
walls.add(wall52)
wall53 = Object(wall, 900, 720, 0)
all_sprites.add(wall53)
walls.add(wall53)
wall54 = Object(wall, 990, 720, 0)
all_sprites.add(wall54)
walls.add(wall54)
wall55 = Object(wall, 1080, 720, 0)
all_sprites.add(wall55)
walls.add(wall55)
wall56 = Object(wall, 1170, 720, 0)
all_sprites.add(wall56)
walls.add(wall56)
wall57 = Object(wall, 1280, 720, 0)
all_sprites.add(wall57)
walls.add(wall57)

wall60 = Object(wall, -115, 90, 0)
all_sprites.add(wall60)
walls.add(wall60)
wall61 = Object(wall, -115, 180, 0)
all_sprites.add(wall61)
walls.add(wall61)
wall62 = Object(wall, -115, 270, 0)
all_sprites.add(wall62)
walls.add(wall62)
wall63 = Object(wall, -115, 360, 0)
all_sprites.add(wall63)
walls.add(wall63)
wall64 = Object(wall, -115, 450, 0)
all_sprites.add(wall64)
walls.add(wall64)
wall65 = Object(wall, -115, 540, 0)
all_sprites.add(wall65)
walls.add(wall65)
wall66 = Object(wall, -115, 630, 0)
all_sprites.add(wall66)
walls.add(wall66)
wall67 = Object(wall, -115, 720, 0)
all_sprites.add(wall67)
walls.add(wall67)

#Стенки

points = 0 #Количество очков(собранных предметов)

#Текст игры
points_font = pygame.font.Font(None, 40) #Шрифт и размер
points_text = points_font.render("Мана: 0", True, pygame.Color("White")) #Текст, сглаживание и цвет

run = True
while run:
    window.blit(bg, (0, 0)) #Наложение фона
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Выход при нажатии на крестик
            run = False

    keys = pygame.key.get_pressed() #Нажатие на клавиатуру
    #Передвижение игрока
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.rect.y -= player.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.rect.y += player.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.image = player_img
            player.rect.x -= player.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.image = pygame.transform.flip(player_img, True, False)
            player.rect.x += player.speed
        if keys[pygame.K_ESCAPE]:
            run = False

    if len(pygame.sprite.spritecollide(player, walls, False)) > 0 : #Столкновение игрока со стенкой
        player.rect.x = start_x
        player.rect.y = start_y
    if len(pygame.sprite.spritecollide(player, enemies, False)) > 0 : #Столкновение игрока с врагом
        player.rect.x = start_x
        player.rect.y = start_y
    if len(pygame.sprite.spritecollide(player, items, True)) > 0 : #Столкновение игрока с вещью(маной)
        points += 1
        points_text = points_font.render("Мана: " + str(points), True, pygame.Color("White"))

    #Движение врагов

    enemy1.rect.x += enemy1.speed
    enemy2.rect.x += enemy2.speed
    enemy3.rect.y += enemy3.speed 

    #Столкновение врагов со стенками

    if len(pygame.sprite.spritecollide(enemy1, walls, False)) > 0 :
        enemy1.speed *= -1
        if enemy1.speed > 0:
            enemy1.image = enemy_img
        else: 
            enemy1.image = pygame.transform.flip(enemy_img, True, False)
    if len(pygame.sprite.spritecollide(enemy2, walls, False)) > 0 :
        enemy2.speed *= -1
        if enemy2.speed > 0:
            enemy2.image = enemy_img
        else: 
            enemy2.image = pygame.transform.flip(enemy_img, True, False)
    if len(pygame.sprite.spritecollide(enemy3, walls, False)) > 0 :
        enemy3.speed *= -1


    all_sprites.draw(window) #Отображение спрайтов в окне
    all_sprites.update() #Обновление спрайтов
    window.blit(points_text, (30, 30)) #Отображение текста
    pygame.display.update() #Обновление экрана