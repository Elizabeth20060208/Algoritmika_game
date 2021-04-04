import pygame
window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) #Размер игрового окна
pygame.display.set_caption("Алгоритмика") #Название программы

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
player_img = pygame.transform.scale(pygame.image.load("images/player.png"), (60, 65)) #Загрузка игрока с компьютера
wall = pygame.transform.scale(pygame.image.load("images/wall.png"), (120, 100)) #Загрузка стенок с компьютера(дерева)
enemy_img = pygame.transform.scale(pygame.image.load("images/enemy.png"), (60, 65)) #Загрузка врага с компьютера

all_sprites = pygame.sprite.Group() #Создание группы объектов
walls = pygame.sprite.Group() #Создание группы стенок
enemies = pygame.sprite.Group() #Создание группы врагов

player = Object(player_img, start_x, start_y, 4) #Создание объекта "игрок"
all_sprites.add(player) #Добавление объекта "игрок" в группу всех спрайтов

enemy1 = Object(enemy_img, 800, 150, 4) #Создание объекта "враг1"
all_sprites.add(enemy1) #Добавление объекта "враг1" в группу всех спрайтов
enemies.add(enemy1) #Добавление объекта "враг1" в группу "враги"
enemy2 = Object(enemy_img, 500, 470, 4)
all_sprites.add(enemy2)
enemies.add(enemy2)
enemy3 = Object(enemy_img, 250, 300, 4)
all_sprites.add(enemy3)
enemies.add(enemy3)


#Стенки

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
wall26 = Object(wall, 1160, 0, 0)
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

#Стенки


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

    if len(pygame.sprite.spritecollide(player, walls, False)) > 0: #Столкновение игрока со стенкой
        player.rect.x = start_x
        player.rect.y = start_y
    if len(pygame.sprite.spritecollide(player, enemies, False)) > 0 : #Столкновение игрока с врагом
        player.rect.x = start_x
        player.rect.y = start_y

    #Движение врагов

    enemy1.rect.x += enemy1.speed
    enemy2.rect.x += enemy2.speed
    enemy3.rect.y += enemy3.speed 

    #Столкновение врагов со стенками

    if len(pygame.sprite.spritecollide(enemy1, walls, False)) > 0 :
        enemy1.speed *= -1
    if len(pygame.sprite.spritecollide(enemy2, walls, False)) > 0 :
        enemy2.speed *= -1
    if len(pygame.sprite.spritecollide(enemy3, walls, False)) > 0 :
        enemy3.speed *= -1

    all_sprites.draw(window) #Отображение спрайтов в окне
    all_sprites.update() #Обновление спрайтов
    pygame.display.update() #Обновление экрана